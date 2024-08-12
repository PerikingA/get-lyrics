import re

def get_info(song_string):
    # Pattern to match the song title and artist
    pattern = re.compile(r"^(.*?)(?: \(feat\..*?\))? by (.+)$")
    
    match = pattern.match(song_string)
    
    if match:
        title = match[1].strip()
        artist = match[2].strip()
        return title, artist
    else:
        raise ValueError("Input string must be in the format '{song title} by {artist}'")

# print(get_info("by and by by caamp"))  # Should return ("by and by", "caamp")
# print(get_info("Saturday Mornings (feat. Lil Wayne) by Cordae"))  # Should return ("Saturday Mornings", "Cordae")
