from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
movies_content = response.text

soup = BeautifulSoup(movies_content, 'html.parser')

all_movies = soup.find_all(name='h3', class_='jsx-4245974604')
all_movies_list = [movie.getText() for movie in all_movies]

movies = all_movies_list[::-1]

with open('movies.txt', mode='w') as file:
    for movie in movies:
        file.write(f'{movie}\n')
