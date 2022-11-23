import requests
import bs4 

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page =response.text

soup = bs4.BeautifulSoup(web_page, "html.parser")

p = soup.find_all(name="h3", class_="title")
# print(p)

movie_title = [movie.getText() for movie in p]
print(movie_title[::-1])
