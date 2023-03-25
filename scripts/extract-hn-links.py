import argparse
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Extract links posted in the comments on a hacker news thread')
parser.add_argument('url', help='URL of the hacker news thread')

args = parser.parse_args()

response = requests.get(args.url)
soup = BeautifulSoup(response.text, 'html.parser')
unique_links = set()

links = soup.select('.comment-tree .athing .comment a')

for link in links:
    title = link.get_text()
    if title.startswith('reply'):
        continue
    href = link['href']
    if href not in unique_links:
        unique_links.add((title,href))
for link in unique_links:
    markdown_link = f"[{link[0]}]({link[1]})"
    print(markdown_link)
