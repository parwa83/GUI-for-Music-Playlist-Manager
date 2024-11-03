import song

class Node:
    def __init__(self, song):
        self.song = song
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, new_song):
        if not self.head:
            self.head = Node(new_song)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(new_song)

    def remove_song(self, title):
        current = self.head
        prev = None
        while current and current.song.title != title:
            prev = current
            current = current.next
        if current is None:
            return False
        if prev is None:
            self.head = current.next
        else:
            prev.next = current.next
        return True

    def display_playlist(self):
        songs = []
        current = self.head
        position = 1
        while current:
            songs.append(f"{position}. {current.song}")
            current = current.next
            position += 1
        return "\n".join(songs)

    def search_song(self, keyword):
        current = self.head
        position = 1
        while current:
            if keyword.lower() in current.song.title.lower() or keyword.lower() in current.song.artist.lower():
                return f"Found '{current.song}' at position {position}"
            current = current.next
            position += 1
        return "Song not found."

    def reverse_playlist(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
