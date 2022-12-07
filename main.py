# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from imdb import Cinemagoer

import requests
from bs4 import BeautifulSoup



def get_movies(url):
    #country_lists = ['de','ar','es','ie','gb','us']
    page = requests.get(url)
    soup = BeautifulSoup(page.text,parser='lxml')
    results = list()
    for link in soup.find_all('a'):
      if '/tt' in link.get('href') and not ('vote' in link.get('href')) and not ('plotsummary' in link.get('href')):
        results.append(link.get('href'))
    if '201' in url:
        print()
    for link in soup.find_all('a'):
      if 'Next »' in link.text:
        print(f"Next Page! {link.get('href')}")
        results.extend(get_movies(f"https://www.imdb.com/{link.get('href')}"))
        break
    # Make results unique, convert to dict, and then to list
    results = list(dict.fromkeys(results))
    print(f"# of results: {len(results)}")
    return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    url = "https://www.imdb.com/search/title/?title_type=feature&user_rating=7.0,&num_votes=1000,&countries=!in&count=500&release_date=2021-01-01,"
    results = get_movies(url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
