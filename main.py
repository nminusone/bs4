from bs4 import BeautifulSoup
import requests
import re

response = requests.get("https://news.ycombinator.com/")
print(response)
hacker_soup = BeautifulSoup(response.text, "html.parser")
# print(hacker_soup.prettify())
titles = hacker_soup.find_all(name="a", class_="titlelink")
title_text = [title.get_text() for title in titles]
article_link = [link.get("href") for link in titles]
upvotes = hacker_soup.find_all(name="span", class_="score")
votes = [upvote.get_text() for upvote in upvotes]

str_votes = [item.split() for item in votes]
vote_count = [int(lists[0]) for lists in str_votes]

print(vote_count)

max_index= vote_count.index(max(vote_count))
print(max_index)
print(title_text[max_index], article_link[max_index], vote_count[max_index])

# with open("website.html", encoding="utf8") as website:
#     contents = website.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
#
# # print(soup.a)
# anchor_tags = soup.find_all(name="a")
#
# anchor_text = [tag.getText() for tag in anchor_tags]
#
# # Useful functions
# #   tag.get("href")
# heading = soup.find(name="h1", id="name")
# print(anchor_text)
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get_text())
# company_url=soup.select_one(selector="p a")
# print(company_url)
# headings= soup.select(".heading")
# print(headings)
