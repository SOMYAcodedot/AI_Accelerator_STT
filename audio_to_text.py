#-------------------------------------------------------------------------------------------------
# Import necessary modules and load config
#-------------------------------------------------------------------------------------------------

import os
import logging
from config import settings  # load paths and models from centralized config

#-------------------------------------------------------------------------------------------------
# Set up basic logger to track activity
#-------------------------------------------------------------------------------------------------
logging.basicConfig(
    filename="transcription.log",
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)
logger = logging.getLogger()

#-------------------------------------------------------------------------------------------------
# Load variables from config
#-------------------------------------------------------------------------------------------------
model = settings["WHISPER_MODEL"]
audio_dir = settings["AUDIO_DIR"]
output_dir = "transcripts"

#-------------------------------------------------------------------------------------------------
# Create transcripts folder if it doesn't exist
#-------------------------------------------------------------------------------------------------
os.makedirs(output_dir, exist_ok=True)
logger.info(f"Transcripts folder ensured at: {output_dir}")

#-------------------------------------------------------------------------------------------------
# Find supported audio files
#-------------------------------------------------------------------------------------------------
supported_formats = ('.mp3', '.wav', '.m4a')
audio_files = [f for f in os.listdir(audio_dir) if f.endswith(supported_formats)]
logger.info(f"Found {len(audio_files)} audio files in '{audio_dir}'")

#-------------------------------------------------------------------------------------------------
# Transcribe each file and save the text output
#-------------------------------------------------------------------------------------------------
for file_name in audio_files:
    file_path = os.path.join(audio_dir, file_name)
    logger.info(f"Processing: {file_name}")
    print(f"Processing: {file_name}")
    
    try:
        result = model.transcribe(file_path)
        transcript_text = result["text"]
        
        output_file = os.path.splitext(file_name)[0] + ".txt"
        output_path = os.path.join(output_dir, output_file)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(transcript_text)
        
        logger.info(f"Transcription saved as: {output_file}")
    except Exception as e:
        logger.error(f"Error during transcription for '{file_name}': {e}")

#-------------------------------------------------------------------------------------------------
# Completion log
#-------------------------------------------------------------------------------------------------
print("Transcription complete. Check the 'transcripts' folder.")
logger.info("All audio files processed successfully.")