import os
from bs4 import BeautifulSoup
import requests
import urllib.request


# def Mreview():
#     page = requests.get('https://movie.naver.com/movie/board/review/list.nhn')
#     html = page.text
#     soup = BeautifulSoup(html,'lxml')
#     print(soup)


def Mrank():
    page = requests.get('https://movie.naver.com/movie/running/current.nhn')
    html = page.text
    soup = BeautifulSoup(html,'lxml')

    # 영화 상영 정보
    titles=soup.find_all('dl','lst_dsc')
    moviedata = []
    for i in titles:
        mdata = {}
        #제목 저장
        tdata = i.find('dt','tit')
        tdata = tdata.find('a').text
        mdata['title'] = tdata
        # print(mdata)

        #평점
        star = i.find('div','star_t1')
        star = star.find('span','num')
        mdata['star']=star.text
        # print(mdata)

        #장르
        genre = i.find('dl','info_txt1')
        genre = genre.find('span','link_txt').text
        genre = genre.replace('\n','').replace('\t','').replace('\r','')
        mdata['genre']=genre

        moviedata.append(mdata)
        # print(mdata)


    #영화 이미지 정보
    imgresult = soup.find_all('div','thumb')
    imgurl = []
    for j in imgresult:
        url = j.find('img')
        imgurl.append(url['src'])
        # print(url['src'])

    cnt =0
    for k in moviedata:
        k['img'] =imgurl[cnt]
        cnt +=1

    return moviedata







# html = urllib.request.urlopen('https://movie.naver.com/movie/running/current.nhn')
# soup = BeautifulSoup(html,'lxml')
# # print(soup)

# titles=soup.find_all('dl','lst_dsc')
# print(titles)

# rank =1
# count =0
# for title in titles:
#     print(str(rank)+"위:",title.find('a').text)
#     rank +=1
#     count +=1
#     if count == 10:
#         break
#
# images=soup.find_all()