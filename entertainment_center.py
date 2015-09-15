#Importing all important class as well fresh tomato file for rendering
import media
import fresh_tomatoes

# Initialization of Movie Objects with my favorite movies
toy_story = media.Movie("Toy Story","A story of boy and his toys","https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=fPhse4WlgEA")

ratatouille = media.Movie("Ratatouille","A story of Chef Rat","https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")

toy_story3 = media.Movie("Toy Story 3","A story of relationships of personified toys","https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg","https://www.youtube.com/watch?v=JcpWXaA2qeg");

gattaca = media.Movie("Gattaca","A story utiopian universe where people are judged from genetic potential","https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg","https://www.youtube.com/watch?v=ZppWok6SX88")

matrix = media.Movie("Matrix","A story of dystopian universe where every person lives in a digital illusion","https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg","https://www.youtube.com/watch?v=m8e-FF8MsqU")

harry_potter = media.Movie("Harry Potter","A story of friendship","https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg","https://www.youtube.com/watch?v=YzfEH0UPEBo")

spiderman = media.Movie("Spiderman(2002)","A story of a rising of a superhero","https://upload.wikimedia.org/wikipedia/en/f/f3/Spider-Man2002Poster.jpg","https://www.youtube.com/watch?v=O7zvehDxttM")

dark_knight = media.Movie("Dark Knight","A story of conflict between chaos and order","https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg","https://www.youtube.com/watch?v=EXeTwQWrcwY")
#Movie list
movies = [toy_story, ratatouille,toy_story3,gattaca,matrix,harry_potter,spiderman,dark_knight]

# Fresh Tomatoes takes all the movie list and renders it on html
fresh_tomatoes.open_movies_page(movies)
