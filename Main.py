import tkinter as tk
from tkinter import messagebox, simpledialog
from playlist import Playlist
from song import Song

class PlaylistManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Playlist Manager")

        self.playlist = Playlist()

        # Interface Elements
        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Song", command=self.remove_song)
        self.remove_button.pack()

        self.display_button = tk.Button(root, text="Display Playlist", command=self.display_playlist)
        self.display_button.pack()

        self.search_button = tk.Button(root, text="Search Song", command=self.search_song)
        self.search_button.pack()

        self.reverse_button = tk.Button(root, text="Reverse Playlist", command=self.reverse_playlist)
        self.reverse_button.pack()

        self.playlist_text = tk.Text(root, width=50, height=15)
        self.playlist_text.pack()

    def add_song(self):
        title = simpledialog.askstring("Input", "Enter song title:")
        artist = simpledialog.askstring("Input", "Enter song artist:")
        duration = simpledialog.askfloat("Input", "Enter song duration (mins):")
        if title and artist and duration:
            new_song = Song(title, artist, duration)
            self.playlist.add_song(new_song)
            messagebox.showinfo("Success", "Song added to playlist!")
        else:
            messagebox.showerror("Error", "All fields must be filled.")

    def remove_song(self):
        title = simpledialog.askstring("Input", "Enter song title to remove:")
        if self.playlist.remove_song(title):
            messagebox.showinfo("Success", "Song removed from playlist!")
        else:
            messagebox.showerror("Error", "Song not found in playlist.")

    def display_playlist(self):
        playlist_str = self.playlist.display_playlist()
        self.playlist_text.delete(1.0, tk.END)
        if playlist_str:
            self.playlist_text.insert(tk.END, playlist_str)
        else:
            self.playlist_text.insert(tk.END, "Playlist is empty.")

    def search_song(self):
        keyword = simpledialog.askstring("Input", "Enter title or artist to search:")
        result = self.playlist.search_song(keyword)
        messagebox.showinfo("Search Result", result)

    def reverse_playlist(self):
        self.playlist.reverse_playlist()
        messagebox.showinfo("Success", "Playlist order reversed.")
        self.display_playlist()

if __name__ == "__main__":
    root = tk.Tk()
    app = PlaylistManagerApp(root)
    root.mainloop()
