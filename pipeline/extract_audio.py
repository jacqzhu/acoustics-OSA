from moviepy.editor import VideoFileClip

video_path = r"R:\Speech and Craniofacial analysis\Collected Data\UMich Data\April_16_2025\03_DCSF0094.avi"
audio_path = r"C:\Users\AkbarS\Desktop\Jacqueline\audio\03_DCSF0094 (1).wav"

def extract_audio(video_path, audio_path):
    # Load video file
    video = VideoFileClip(video_path)
    # Extract and write audio
    if video.audio is not None:
        video.audio.write_audiofile(audio_path)
        print(f"Audio extracted and saved to {audio_path}")
    else:
        print("No audio stream found in the video.")

# Example usage:
extract_audio(video_path, audio_path)