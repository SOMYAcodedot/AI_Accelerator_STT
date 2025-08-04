#config.py
import os
import whisper
whisper_model = whisper.load_model("base")
audio_dir = "audio_data"  # change this to your actual folder path



def load_api_keys():

   
    return {
        "AUDIO_DIR" : audio_dir,
        "WHISPER_MODEL" : whisper_model
    }
 
settings = load_api_keys()
 


