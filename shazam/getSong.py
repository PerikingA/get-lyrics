import requests

from shazam.recordAudio import record_audio
from shazam.processAudio import raw_file2base64, send_post_request
from shazam.getSongInfo import get_song_info

# from recordAudio import record_audio
# from processAudio import raw_file2base64, send_post_request
# from getSongInfo import get_song_info

def get_song():
    
    try:
        audio = record_audio()
        payload = raw_file2base64(audio)
        response = send_post_request(payload)
        response.raise_for_status() 
        
        info = get_song_info(response.json())
        print(info)
        return get_song_info(response.json())
    except requests.exceptions.RequestException as e:
        print(f"HTTP Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# get_song()