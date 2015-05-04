# entertainment_center.py
# contains descriptions and relevant media links for 
# each movie object instance


import fresh_tomatoes
import media

amadeus = media.Movie("Amadeus",
                        "The incredible story of Wolfgang Amadeus Mozart, told by his peer and secret rival Antonio Salieri - now confined to an insane asylum.",
                        "http://upload.wikimedia.org/wikipedia/en/thumb/2/2f/Amadeusmov.jpg/220px-Amadeusmov.jpg",
                        "https://www.youtube.com/watch?v=yIzhAKtEzY0")

magnolia = media.Movie("Magnolia",
                     "An epic mosaic of interrelated characters in search of love, forgiveness, and meaning in the San Fernando Valley",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/9/9c/Magnolia_poster.jpg/220px-Magnolia_poster.jpg",
                     "https://www.youtube.com/watch?v=zwXDHSrNFbQ")

princess_bride = media.Movie("The Princess Bride",
                             "A classic fairy tale",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/d/db/Princess_bride.jpg/220px-Princess_bride.jpg",
                             "https://www.youtube.com/watch?v=njZBYfNpWoE")

interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in an attempt to ensure humanity's survival.",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg",
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA")

frozen = media.Movie("Frozen",
                     "When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

gods = media.Movie("The Gods Must Be Crazy",
                  "A comic allegory about a traveling Bushman who encounters modern civilization and its stranger aspects, including a clumsy scientist and a band of revolutionaries",
                  "http://upload.wikimedia.org/wikipedia/en/thumb/5/59/Gods_must_be_crazyposter.jpg/220px-Gods_must_be_crazyposter.jpg",
                  "https://www.youtube.com/watch?v=GorHLQ-jLRQ")


movies = [amadeus, magnolia, princess_bride, interstellar, frozen, gods]                   
# This list of movie objects is passed to the function that follows

fresh_tomatoes.open_movies_page(movies)
# The html file is now created.





                                                    

















