import moviepy.editor as mp
from os import path

def convert_video_to_audio():
    # Assign files
    input_file = "elgato.mp4"
    output_file = "elgato.mp3"
    
    # Check if the audio file already exists
    if not path.exists(output_file):
        # Insert Local Video File Path
        clip = mp.VideoFileClip(input_file)
        
        # Insert Local Audio File Path
        clip.audio.write_audiofile(output_file)
        print(f"Converted {input_file} to {output_file}")
    else:
        print(f"{output_file} already exists. Skipping conversion.")

# Call the function
convert_video_to_audio()
