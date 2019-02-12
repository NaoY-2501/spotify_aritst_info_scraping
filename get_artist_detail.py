import json
import re
import requests

from bs4 import BeautifulSoup as bs

URL = 'https://open.spotify.com/artist/{artist_id}/about'

ARTIST_ID = '2dEKl1tM3JMwggawEuVISO'

def get_detail(artist_id):
    url = URL.format(artist_id=artist_id)
    res = requests.get(url)
    soup = bs(res.content, features='html.parser')
    scripts = soup.find_all('script')
    print(len(scripts))


if __name__ == '__main__':
    get_detail(ARTIST_ID)
