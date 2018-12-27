import media
import fresh_tomatoes

#Defined values of attributes for each movie
avengers = media.Movie("Avengers",
                       "Earth's mightiest heroes must come together and " +
                       "learn to fight as a team if they are going to stop" +
                       " the mischievous Loki and his alien army from" +
                       "enslaving humanity.",
                       "https://upload.wikimedia.org/wikipedia/en/" +
                       "f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

avengers2 = media.Movie("Avengers Age of Ultron",
                        "Earth's mightiest heroes must come together and " +
                        "learn to fight as a team if they are going to " +
                        "stop the Ultron from enslaving humanity.",
                        "https://upload.wikimedia.org/wikipedia/pt/" +
                        "2/22/OsVingadores2.jpg",
                        "https://www.youtube.com/watch?v=tmeOjFno6Do")

avengers3 = media.Movie("Avengers Infinity War",
                        "Earth's mightiest heroes must come together and " +
                        "learn to fight as a team if they are going to " +
                        "stop the Thanos from enslaving humanity.",
                        "https://upload.wikimedia.org/wikipedia/pt/" +
                        "9/90/Avengers_Infinity_War.jpg",
                        "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

avengers4 = media.Movie("Avengers End Game",
                        "Earth's mightiest heroes must come together and " +
                        "learn to fight as a team if they are going to " +
                        "stop the Thanos from enslaving humanity.",
                        "https://upload.wikimedia.org/wikipedia/en/" +
                        "0/0d/Avengers_Endgame_poster.jpg",
                        "https://www.youtube.com/watch?v=hA6hldpSTF8")

movies = [avengers, avengers2, avengers3, avengers4]

# Calling open_movies_page function from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)