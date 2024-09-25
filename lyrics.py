import lyricsgenius
from dotenv import load_dotenv
import os
import csv

# Load environment variables from the .env file
load_dotenv()

# Get the Genius API key from environment variables
api_key = os.getenv("ACCESS_TOKEN")

# Load the artist names from the text file
with open('artists.txt') as f:
    artists = f.readlines()

artists = [x.strip() for x in artists]

print(artists[50:])

# Initialize the Genius API client
genius = lyricsgenius.Genius(api_key)

# Open a CSV file to store the artist names and lyrics
with open('artists_lyrics.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Artist', 'Song Title', 'Lyrics'])
    
    # Loop through each artist
    for artist in artists[54:]:
        print(f"Fetching songs for artist: {artist}")
        try:
            # Search for the artist
            artist_obj = genius.search_artist(artist, max_songs=10) 
            if artist_obj:
                for song in artist_obj.songs:
                    # Write artist name, song title, and lyrics to the CSV file
                    writer.writerow([artist, song.title, song.lyrics])
                    print(f"Added song: {song.title} by {artist}")
        except Exception as e:
            print(f"An error occurred for artist {artist}: {e}")

print("Lyrics have been successfully saved to 'artists_lyrics.csv'.")
