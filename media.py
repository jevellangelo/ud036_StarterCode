import webbrowser
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'


class Video():
    def __init__(self, title, duration, genre, release_date, poster_image, trailer_youtube):
        print("Parent Constructor Called")
        self.title = title
        self.duration = duration
        self.genre = genre
        self.release_date = release_date
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube



class Movie(Video):
    """This class provides a way to store movie related information"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, genre, release_date, poster_image, trailer_youtube, movie_storyline):
        Video.__init__(self, title, duration, genre, release_date, poster_image, trailer_youtube)
        self.storyline = movie_storyline


    def show_trailer(self):
        webbrowser.get(chrome_path).open(self.trailer_youtube_url)



# class TvShow(Video):
#     def __init__(self, title, duration, genre, release_date, poster_image, trailer_youtube):
#         Video.__init__(self, title, duration, genre, release_date, poster_image, trailer_youtube)
