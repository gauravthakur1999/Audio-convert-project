import requests
from bs4 import BeautifulSoup
import time
import os
import re

# Headers to mimic a real browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to clean and format filenames
def clean_filename(title):
    # Remove invalid characters and replace "_" with " "
    filename = re.sub(r'[\\/*?:"<>|]', "", title).replace("_", " ")[:100]
    return filename

# Function to filter out unwanted lines
def clean_content(content):
    unwanted_phrases = [
        "Search the NovelFire.net website on Google to access chapters of novels early and in the highest quality."
    ]
    cleaned_lines = [line for line in content.split("\n") if line.strip() and line not in unwanted_phrases]
    return "\n".join(cleaned_lines)

# Function to fetch and parse a single chapter
def scrape_chapter(chapter_url):
    try:
        response = requests.get(chapter_url, headers=HEADERS)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract title from <h1><span class="chapter-title">
        title_tag = soup.select_one("h1 span.chapter-title")
        title = title_tag.text.strip() if title_tag else "Unknown Chapter"

        # Extract content from <div id="content">
        content_div = soup.select_one("div#content")
        content = "\n".join([p.text.strip() for p in content_div.find_all("p")]) if content_div else "No content found."

        # Clean the content to remove unwanted text
        content = clean_content(content)

        # Find the next chapter link inside <div class="chapternav skiptranslate py-3 clearfix">
        next_chapter_tag = soup.select_one("div.chapternav.skiptranslate.py-3.clearfix a[title='Next Chapter']")
        next_chapter_url = next_chapter_tag["href"] if next_chapter_tag else None

        # Ensure absolute URL
        if next_chapter_url and not next_chapter_url.startswith("http"):
            next_chapter_url = "https://novelfire.docsachhay.net" + next_chapter_url

        return title, content, next_chapter_url
    except Exception as e:
        print(f"Error scraping {chapter_url}: {e}")
        return None, None, None

# Function to scrape multiple chapters and save each in a different file
def scrape_novel(start_url, num_chapters, save_folder="Webnovel Chapters"):
    os.makedirs(save_folder, exist_ok=True)  # Create folder if not exists
    current_url = start_url

    for i in range(num_chapters):
        print(f"Scraping chapter {i+1}...")

        title, content, next_url = scrape_chapter(current_url)
        if not title or not content:
            print("Skipping this chapter due to an error.")
            break

        # Save each chapter as a separate file
        filename = f"{save_folder}/{clean_filename(title)}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"{title}\n\n{content}\n")

        print(f"Saved: {filename}")

        # Move to the next chapter if available
        if next_url:
            current_url = next_url
        else:
            print("No more chapters found.")
            break

        time.sleep(2)  # Be polite to the server

    print("Scraping completed.")

# Example usage
start_chapter_url = "url here"
num_chapters_to_scrape = 10  # Adjust as needed
scrape_novel(start_chapter_url, num_chapters_to_scrape)
