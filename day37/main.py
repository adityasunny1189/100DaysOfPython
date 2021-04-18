from bs4 import BeautifulSoup
import requests

# Scraping live website

response = requests.get('https://news.ycombinator.com/news')
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

# Create a dictionary out of the content {article_text: [article_link, article_upvote]}
data = {}
articles = soup.find_all(name='a', class_='storylink')
article_upvote = soup.find_all(name='span', class_='score')

for article in articles:
    for score in article_upvote:
        article_text = article.getText()
        article_link = article.get('href')
        data[article_text] = []
        data[article_text].append(article_link)
        score_string = score.getText()
        score_list = score_string.split(' ')
        score_point = int(score_list[0])
        data[article_text].append(score_point)

for news in data:
    print(news, ": ", data[news])

# Print most liked news
top_news = ''
top_news_link = ''
top_news_upvote = 0
for i, j in data.items():
    if j[1] > top_news_upvote:
        top_news = i
        top_news_link = j[0]
        top_news_upvote = j[1]

print(top_news)
print(top_news_link)
print(top_news_upvote)

# article_tag = soup.find(name='a', class_='storylink')
#
# article_content = article_tag.getText()
# article_link = article_tag.get('href')
#
# print(article_content)
# print(article_link)


# all_anchor_tags = soup.find_all(name='a')
#
# for tag in all_anchor_tags:
#     print(tag.text)
#     print(tag.get('href'))

# all_scores = soup.find_all(class_='score')
# print(all_scores)
#
# for score in all_scores:
#     print(score.string)


# response = requests.get('https://google.com')
# google_data = response.text
#
# soup = BeautifulSoup(google_data, 'html.parser')
# title = soup.find(name='title')
# print(title.string)


# with open('website.html') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title.string)
# print(soup.ul.li.string)
#
# all_anchor_tags = soup.findAll(name='a')
# print(all_anchor_tags)
#
# for tags in all_anchor_tags:
#     print(tags.text)
#     print(tags.get('href'))
#
# print(soup.prettify())
# heading = soup.find(name='h3', class_='heading')
# print(heading.string)
# print(soup.text)
