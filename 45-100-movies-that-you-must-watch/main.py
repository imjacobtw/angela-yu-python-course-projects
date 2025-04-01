from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movie_titles_and_rankings = [element.string for element in soup.select("h3.title")]

with open("movies.txt", "w", encoding="ISO-8859-1") as file:
    for entry in reversed(movie_titles_and_rankings):
        file.write(f"{entry}\n")