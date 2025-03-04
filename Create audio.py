import os
from gtts import gTTS

# Folder where text chapters are stored
input_folder = "Webnovel Chapters"
output_folder = "Webnovel Audio"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Get all chapter files and sort them to maintain order
all_chapters = sorted([f for f in os.listdir(input_folder) if f.endswith(".txt")])

# Display available chapters
print("Available Chapters:")
for i, chapter in enumerate(all_chapters):
    print(f"{i + 1}. {chapter}")

# Get user input for starting chapter and number of chapters to convert
start_index = int(input("\nEnter the number of the chapter to start with: ")) - 1
num_chapters = int(input("Enter how many chapters to convert: "))

# Ensure valid input
if start_index < 0 or start_index >= len(all_chapters):
    print("Invalid starting chapter number.")
    exit()
if num_chapters <= 0:
    print("Number of chapters must be greater than 0.")
    exit()

# Function to convert text to audio
def text_to_audio(input_file, output_file):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
        
        if len(text.strip()) == 0:
            print(f"Skipping empty file: {input_file}")
            return
        
        # Convert text to speech
        tts = gTTS(text, lang="en")
        tts.save(output_file)
        print(f"Saved: {output_file}")

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

# Convert selected range of chapters
for i in range(start_index, min(start_index + num_chapters, len(all_chapters))):
    input_path = os.path.join(input_folder, all_chapters[i])
    output_filename = all_chapters[i].replace(".txt", ".mp3")
    output_path = os.path.join(output_folder, output_filename)

    text_to_audio(input_path, output_path)

print("\nSelected chapters converted to audio successfully!")
