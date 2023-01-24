from Inheritance.Need_for_Speed.project import Album

class Band:
    albums = []

    def __init__(self, name):
        self.name = name

    def add_album(self, album: Album):
        if album in Band.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            Band.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for alb in Band.albums:
            if alb.name == album_name:
                if alb.published:
                    return f"Album has been published. It cannot be removed."
                else:
                    Band.albums.remove(alb)
                    return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]
        for bnd in Band.albums:
            result.append(bnd.details())
        return '\n'.join(result)

