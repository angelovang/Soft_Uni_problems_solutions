def add_songs(*songs):
    song_dict = {}
    for element in songs:
        if element[0] not in song_dict:
            song_dict[element[0]] = []
        song_dict[element[0]].extend(element[1])

    result = ''
    for name , lyric in song_dict.items():
        result += f"- {name}\n"
        for el in lyric :
            result += el + '\n'

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
