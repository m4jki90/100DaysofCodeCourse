import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
empire_website = response.text

soup = BeautifulSoup(empire_website, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_list = [movie.getText() for movie in movies]
reversed_list = movie_list[::-1]

with open ("movies.txt", "w") as file:
    for movie in reversed_list:
        file.write(f"{movie} \n")



