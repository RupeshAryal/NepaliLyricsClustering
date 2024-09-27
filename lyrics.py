import lyricsgenius
from dotenv import load_dotenv
import os
import csv

import requests

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


def get_lyrics():
    # Open a CSV file to store the artist names and lyrics
    with open('artists_lyrics.csv', mode='w', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)
        writer.writerow(['Artist', 'Song Title', 'Lyrics'])
        
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

def get_artist_cover_image():
    for artist in artists:
        try:
            artist_image_url = genius.search_artist(artist_name=artist,   max_songs=1).image_url
        except Exception as e:
            artist_image_url = False
        
        if artist_image_url:
            response = requests.get(artist_image_url)

            if response.status_code == 200:
                image_path = "images/" + artist + ".jpg"
                with open(image_path, 'wb') as file:
                    file.write(response.content)

                print(f"Image downloaded successfully for artist: {artist}")

            else:
                print(f"unable to download image. Status Code: {response.status_code}")

        else:
            print(f"No image found for artist {artist}")


get_artist_cover_image()
                


