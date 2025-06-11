class MusicComponent:
    def play(self):
        raise NotImplementedError()


class MusicTrack(MusicComponent):
    def __init__(self, track):
        self.track = track

    def play(self):
        self.track.play()


class Playlist(MusicComponent):
    def __init__(self, name):
        self.name = name
        self.items = []

    def add(self, component: MusicComponent):
        self.items.append(component)

    def remove(self, component: MusicComponent):
        self.items.remove(component)

    def play(self):
        print(f"\nПлейлист: {self.name}")
        for item in self.items:
            item.play()

class RockSong:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def play(self):
        print(f"[Rock] {self.title} — {self.artist} ({self.duration} min)")


class JazzSong:
    def __init__(self, title, artist, instruments):
        self.title = title
        self.artist = artist
        self.instruments = instruments

    def play(self):
        print(f"[Jazz] {self.title} — {self.artist} (Instruments: {', '.join(self.instruments)})")

class MusicLibraryManager:
    def __init__(self):
        self.main_playlist = Playlist("Моя Музична Бібліотека")

    def add_rock_song(self, title, artist, duration):
        song = RockSong(title, artist, duration)
        self.main_playlist.add(MusicTrack(song))

    def add_jazz_song(self, title, artist, instruments):
        song = JazzSong(title, artist, instruments)
        self.main_playlist.add(MusicTrack(song))

    def create_playlist(self, name):
        new_list = Playlist(name)
        self.main_playlist.add(new_list)
        return new_list

    def add_to_playlist(self, playlist: Playlist, item: MusicComponent):
        playlist.add(item)

    def play_all(self):
        self.main_playlist.play()

def run_music_library_demo():
    manager = MusicLibraryManager()

    print("== Додавання треків ==")
    manager.add_rock_song("Thunder Beats", "The Rockers", 3.5)
    manager.add_jazz_song("Smooth Waves", "JazzMind", ["Saxophone", "Piano"])

    print("\n== Створення плейлиста ==")
    favorites = manager.create_playlist("Улюблені")
    manager.add_to_playlist(favorites, MusicTrack(RockSong("Night Drive", "Highway Band", 4)))
    manager.add_to_playlist(favorites, MusicTrack(JazzSong("Golden Hour", "Sunset Trio", ["Trumpet", "Bass"])))

    print("\n== Вміст музичної бібліотеки ==")
    manager.play_all()


if __name__ == "__main__":
    run_music_library_demo()
