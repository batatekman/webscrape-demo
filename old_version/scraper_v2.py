import requests
from bs4 import BeautifulSoup


def get(link):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    url = f'https://www.indeed.co.uk/jobs?q=php+developer&l=London,+Greater+London&radius=50&start={link}'

    req = requests.get(url, user_agent)
    beautifulSoup = BeautifulSoup(req.content, 'html.parser')

    return beautifulSoup


def transform(beautySoup):
    object = beautySoup.find_all('div', class_='jobsearch-SerpJobCard')
    return len(object)


g = get(0)
print(transform(g))
