from project_spotipy.song import Song


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(*songs)
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if self.published:
            return f"Cannot add songs. Album is published."

        if song in self.songs:
            return f"Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        for sng in self.songs:
            if sng.name == song_name:
                self.songs.remove(sng)
                return f"Removed song {song_name} from album {self.name}."
        else:
            return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        result = [f"Album {self.name}"]
        for sng in self.songs:
            result.append(f"== {sng.get_info()}")
        return '\n'.join(result) + "\n"
