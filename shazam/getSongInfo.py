def get_song_info(response_json):
    return response_json.get('track', {}).get('share', {}).get('text', '')
