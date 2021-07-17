from urllib.parse import urlencode, quote_plus

import requests
import json
from bs4 import BeautifulSoup
import re
from collections import Counter


def get_movie():

    userlist = []

    for c in range(1,20):
        url = 'https://movie.naver.com/movie/bi/mi/review.nhn?code=187322&page='+str(c)
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, 'lxml')

        data = soup.find_all('span','user')
        for temp in data:
            uid = re.findall("\d+",str(temp))
            userlist.append(uid[0])

    movietitle_list = []
    for uid in userlist:
        url  = 'https://movie.naver.com/movie/board/review/list.nhn?st=nickname&sword='+uid+'&page=1'
        page = requests.get(url)
        html = page.text
        soup = BeautifulSoup(html, 'lxml')

        movietitle = soup.find_all('td','movie')

        for temp_title in movietitle:
            movietitle_list.append(temp_title.text)



    result = Counter(movietitle_list)
    return result.most_common(4)[1:4]
