# Web Novel Scraper & Text-to-Speech Converter

This project consists of two Python scripts:
1. **novel scraper.py** - Scrapes novel chapters from a website and saves them as text files.
2. **create audio.py** - Converts the scraped text files into audio (.mp3) files using Google Text-to-Speech (gTTS).

---

## **1. Web Novel Scraper**
This script **scrapes novel chapters** from a given starting URL and **saves each chapter separately** in a folder.

### **Installation**
Ensure you have Python installed, then install the required libraries:
```bash
pip install requests beautifulsoup4
```
### **Usage**
Open scrape_novel.py and set the starting chapter URL:
```python
start_chapter_url = "https://your url"
```
Set the number of chapters to scrape:
```python
num_chapters_to_scrape = 10
```
Run the script:
```bash
python novel scarper.py
```
Scraped chapters will be stored as .txt files in the Webnovel Chapters/ folder.
### **Features**
✅ Extracts chapter titles and content from the website.\
✅ Saves each chapter separately in .txt format.\
✅ Follows the next chapter links automatically.\
✅ Handles relative URLs properly.\
✅ Removes unwanted promotional text from the content.\
✅ Ensures proper file naming and avoids invalid characters.

## **2. Text-to-Speech Converter**

This script converts the stored text chapters into audio files (.mp3) using Google Text-to-Speech (gTTS).

Installation
Install gTTS:
```bash
pip install gtts
```
### **Usage**
Run the script:
```bash
python Create audio.py
```
It will list available chapters and prompt you to:
Select the starting chapter by entering the chapter number.
Enter the number of chapters to convert to audio.
Converted .mp3 files will be saved in the The Mech Touch Audio/ folder.
### **Features**
✅ Allows user selection of starting chapter and number of chapters.\
✅ Converts each chapter into a separate .mp3 file.\
✅ Skips empty or corrupted files automatically.\
✅ Maintains correct chapter order.\
✅ Ensures clear, high-quality audio output.

### **Project Structure**
```pgsql
📂 WebNovelScraper
 ├── 📂 Webnovel Chapters        # Scraped chapters stored as .txt files
 ├── 📂 Webnovel Audio           # Converted audio files (.mp3)
 ├── novel scraper.py            # Web scraping script
 ├── create audio.py             # Text-to-speech conversion script
 ├── README.md                   # Project documentation
```

### **Requirements**
Python 3.7+
Required Python Libraries:
```bash
pip install requests beautifulsoup4 gtts
```

Notes
* Scraping must comply with the website’s Terms of Service.
* The gTTS library requires an internet connection to process text-to-speech.
* If any issues arise, check the HTML structure of the website and update selectors accordingly.

### **Author**
Developed by Gaurav Thakur 🚀
For any improvements or issues, feel free to contribute!
