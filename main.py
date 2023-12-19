import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


def request_movie_site_contents():
    response = requests.get(url=URL)
    response.raise_for_status()
    return response.text


def get_movie_list():
    movie_site_contents = request_movie_site_contents()
    soup = BeautifulSoup(movie_site_contents, "html.parser")
    # print(soup.prettify())
    return [title.get_text() for title in soup.find_all(name="h3", class_="title")][::-1]


def write_movie_list_to_file(movies):
    with open("movies.txt", "w", encoding="utf-8") as file:
        for movie in movies:
            file.write(movie + "\n")


movie_list = get_movie_list()
write_movie_list_to_file(movie_list)
