from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for row in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE))

    def add_photo(self,label:str):
        for row in range(self.pages):
            if len(self.photos[row]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[row].append(label)

                return f"{label} photo added successfully on page {row+1} slot {len(self.photos[row])}"

        return f"No more free slots"

    def display(self):
        result = ['-'*11]
        for row in self.photos:
            result.append(f"{('[] '*len(row)).rstrip()}")
            result.append('-'*11)

        return '\n'.join(result)

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())