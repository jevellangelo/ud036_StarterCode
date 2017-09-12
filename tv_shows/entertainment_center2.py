import fresh_tomatoes
import media

fight_club = media.Movie("Fight Club",
                        "2h 19min",
                        "Drama",
                        "15 October 1999",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=BdJKm16Co6M",
                        "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.")
# print(fight_club.storyline)

avatar = media.Movie("Avatar",
                     "2h 42min",
                     "Action, Adventure, Fantasy",
                     "18 December 2009",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4",
                     "A marine on an alien planet")

friday = media.Movie("Friday",
                     "1h 31min",
                     "Comedy, Drama",
                     "26 April 1995",
                     "https://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg",
                     "https://www.youtube.com/watch?v=sujATt9Ur0o",
                     "Two homies, Smokey and Craig, smoke a dope dealer's weed and try to figure a way to get the $200 they owe to the dealer by 10 p.m. that same night.")

# print(avatar.storyline)
# avatar.show_trailer()
# friday.show_trailer()

the_matrix = media.Movie("The Matrix",
                         "2h 16min",
                         "Action, Sci-Fi",
                         "31 March 1999",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=a94b1yZOBes",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.")

rounders = media.Movie("Rounders",
                       "2h 1min",
                       "Crime, Drama",
                       "11 September 1998",
                       "https://upload.wikimedia.org/wikipedia/en/6/67/RoundersPoster.jpg",
                       "https://www.youtube.com/watch?v=sV5f97wqeW4",
                       "A young man is a reformed gambler who must return to playing big stakes poker to help a friend pay off loan sharks, while balancing his relationship with his girlfriend and his commitments to law school.")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "2h 22min",
                                       "Crime, Drama",
                                       "14 October 1994",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                       "https://www.youtube.com/watch?v=K_tLp7T6U1c",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.")

movies = [fight_club, avatar, friday, the_matrix, rounders, the_shawshank_redemption]
# tv_shows
# tv_shows = []
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
# print(media.Movie.__doc__)

# print("The name of class I created is " + media.Movie.__name__)

# print("The module is called " + media.Movie.__module__)
