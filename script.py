import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import tkinter as tk
from tkinter import simpledialog

def get_playlist_tracks():
    def submit():
        nonlocal client_id_entry, client_secret_entry, playlist_id_entry, date_entry

        client_id = client_id_entry.get()
        client_secret = client_secret_entry.get()
        playlist_id = playlist_id_entry.get()
        date = date_entry.get()

        if client_id and client_secret and playlist_id and date:
            root.destroy()
            get_tracks(client_id, client_secret, playlist_id, date)
        else:
            error_label.config(text="Please fill in all fields")

    root = tk.Tk()
    root.title("Spotify Playlist Tracks")
    root.geometry("400x300")  # Set window size

    client_id_label = tk.Label(root, text="Spotify Client ID:", width=15)
    client_id_entry = tk.Entry(root, width=30)  # Set entry field size

    client_secret_label = tk.Label(root, text="Spotify Client Secret:", width=15)
    client_secret_entry = tk.Entry(root, show="*", width=30)  # Set entry field size

    playlist_id_label = tk.Label(root, text="Playlist ID:", width=15)
    playlist_id_entry = tk.Entry(root, width=30)  # Set entry field size

    date_label = tk.Label(root, text="Date (YYYY-MM-DD):", width=15)
    date_entry = tk.Entry(root, width=30)  # Set entry field size

    submit_button = tk.Button(root, text="Submit", command=submit)
    error_label = tk.Label(root, fg="red")

    client_id_label.pack()
    client_id_entry.pack()
    client_secret_label.pack()
    client_secret_entry.pack()
    playlist_id_label.pack()
    playlist_id_entry.pack()
    date_label.pack()
    date_entry.pack()
    submit_button.pack()
    error_label.pack()

    root.mainloop()

def get_tracks(client_id, client_secret, playlist_id, date):
    try:
        # Initialize Spotipy with provided credentials
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

        # Retrieve all tracks from the specified playlist
        results = sp.playlist_tracks(playlist_id, fields='items(added_at,track(name,artists))', additional_types=['track'], market='US')

        # Extract tracks added after the specified date
        tracks = results['items']
        filtered_tracks = [track for track in tracks if track['added_at'] >= date]

        if filtered_tracks:
            print(f"Songs in the playlist added after {date}:")
            for track in filtered_tracks:
                track_info = track['track']
                track_name = track_info['name']
                artists = ', '.join([artist['name'] for artist in track_info['artists']])
                added_at = track['added_at']
                print(f"{track_name} by {artists} (Added at: {added_at})")
        else:
            print("No tracks found.")
    
    except Exception as e:
        print("Error:", e)

get_playlist_tracks()
