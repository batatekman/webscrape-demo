import requests
from bs4 import BeautifulSoup
import pandas as pd


# Get Initial settings made
# User Agent + URL
# use BeautifulSoup and html.parser
# ready to scrape data


def get(link):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    url = f'https://www.indeed.co.uk/jobs?q=php+developer&l=London,+Greater+London&radius=50&start={link}'

    req = requests.get(url, user_agent)
    beautifulSoup = BeautifulSoup(req.content, 'html.parser')

    return beautifulSoup

# transform method used
# scrape data and add
# to dictionary file
# 'jobsItemList'


def transform(beautySoup):
    divObject = beautySoup.find_all('div', class_='jobsearch-SerpJobCard')
    mcount = 0
    for blocks in divObject:
        title = blocks.find('a').text.strip()
        company = blocks.find('span', class_='company').text.strip()
        address = blocks.find(
            'span', class_='location accessible-contrast-color-location').text.split()

        print(title)
        print(company)
        print(address)
        try:
            salary = blocks.find('span', class_='salaryText').text.strip()
            print(salary)
        except:
            salary = ''
            print('')

        try:
            summary = blocks.find(
                'div', class_='summary').text.strip().replace('\n', '')
            print(summary)
        except:
            print('')

        jobitem = {
            'title': title,
            'company': company,
            'address': address,
            'salary': salary,
            'summary': summary
        }

        jobItemsList.append(jobitem)

        print("\r\n")
        mcount += 1

    print("\r\nJobs on this page ", mcount)
    return


# Dictionary File
jobItemsList = []

# Loop through website starting
# at 0 with 30 items and 10 per
# page
for i in range(0, 30, 10):
    print(f'Retrieving page... {i}')
    g = get(0)
    transform(g)

print("Results returned ", len(jobItemsList))

dataFrame = pd.DataFrame(jobItemsList)
print(dataFrame.head())
dataFrame.to_csv('jobs.csv')
