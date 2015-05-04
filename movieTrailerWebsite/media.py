# media.py
# defines the Movie class used in entertainment_center.py to create movie instances

import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] 
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    def show_trailer(self):
        """This method of the Movie class opens the relevant trailer in a web browser"""
        webbrowser.open(self.trailer_youtube_url)
        
