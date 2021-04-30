from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.youtube.com/results?search_query=covid+in+india&sp=EgIIAg%253D%253D')
soup = BeautifulSoup(response.text, 'html.parser')
# all_video_link = soup.find_all('a', {'class': 'pl-video-title-link'})
# print(all_video_link)

print(soup.prettify())
