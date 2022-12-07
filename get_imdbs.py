import datetime

import requests
from bs4 import BeautifulSoup



def get_movies(url):
    #country_lists = ['de','ar','es','ie','gb','us']
    page = requests.get(url)
    soup = BeautifulSoup(page.text, features='lxml')
    results = list()
    for link in soup.find_all('a'):
      if '/tt' in link.get('href') and not ('vote' in link.get('href')) and not ('plotsummary' in link.get('href')):
        results.append(link.get('href').split("/")[2])
    for link in soup.find_all('a'):
      if 'Next »' in link.text:
        print(f"{datetime.datetime.now()} || Next Page! {link.get('href')}")
        results.extend(get_movies(f"https://www.imdb.com/{link.get('href')}"))
        break
    # Make results unique, convert to dict, and then to list
    results = list(dict.fromkeys(results))
    print(f"{datetime.datetime.now()} || # of results: {len(results)}")
    return results

def get_cool_movies():
  min_votes = 900
  max_votes = ""
  excluded_countries = '!in,!pk,!bd'
  items_per_page = 50
  minimum_release_date = '2021-01-01'
  maximum_release_date = ''
  minimum_rating = 6.9
  url = f"https://www.imdb.com/search/title/?title_type=feature&user_rating={minimum_rating},&num_votes={min_votes},{max_votes}&countries={excluded_countries}&count={items_per_page}&release_date={minimum_release_date},{maximum_release_date}"
  results = get_movies(url)
  return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    min_votes = 900
    max_votes = ""
    excluded_countries = 'in'
    items_per_page= 50
    minimum_release_date = '2021-01-01'
    maximum_release_date = ''
    minimum_rating = 6.9
    url = f"https://www.imdb.com/search/title/?title_type=feature&user_rating={minimum_rating},&num_votes={min_votes},{max_votes}&countries=!{excluded_countries}&count={items_per_page}&release_date={minimum_release_date},{maximum_release_date}"
    results = get_movies(url)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
