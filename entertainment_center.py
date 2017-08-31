import fresh_tomatoes
import media

fight_club = media.Movie("Fight Club",
                        "An insomniac office worker, looking for a way to change his life, crosses paths with a devil-may-care soap maker, forming an underground fight club that evolves into something much, much more.",
                        "https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg",
                        "https://www.youtube.com/watch?v=BdJKm16Co6M")
# print(fight_club.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")

friday = media.Movie("Friday",
                     "Two homies, Smokey and Craig, smoke a dope dealer's weed and try to figure a way to get the $200 they owe to the dealer by 10 p.m. that same night.",
                     "https://upload.wikimedia.org/wikipedia/en/2/27/Fridayposter1995.jpg",
                     "https://www.youtube.com/watch?v=sujATt9Ur0o")

# print(avatar.storyline)
# avatar.show_trailer()
# friday.show_trailer()

the_matrix = media.Movie("The Matrix",
                         "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=a94b1yZOBes")

rounders = media.Movie("Rounders",
                       "A young man is a reformed gambler who must return to playing big stakes poker to help a friend pay off loan sharks, while balancing his relationship with his girlfriend and his commitments to law school.",
                       "https://upload.wikimedia.org/wikipedia/en/6/67/RoundersPoster.jpg",
                       "https://www.youtube.com/watch?v=sV5f97wqeW4")

the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                       "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.",
                                       "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                                       "https://www.youtube.com/watch?v=K_tLp7T6U1c")

movies = [fight_club, avatar, friday, the_matrix, rounders, the_shawshank_redemption]
# fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)

print("The name of class I created is " + media.Movie.__name__)

print("The module is called " + media.Movie.__module__)
