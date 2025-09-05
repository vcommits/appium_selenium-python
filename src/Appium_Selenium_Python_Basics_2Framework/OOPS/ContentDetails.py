class ContentDetails:
    def __init__(self, album,artist,track):
    def contentInfo(self, album, artist, track):
        print("Album :", album)
        print("Artist :", artist)
        print("Track :", track)

    def albumInfo(self):
        pass


cdi = ContentDetails()

cdi.contentInfo("B.B. Live At The Forum!", "B.B. King", "Thrill is Gone")