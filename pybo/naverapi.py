import urllib.request
import json

def naverbook(bookname):

    client_id = "01aH03vjnHWIg5SacVqp"
    client_secret = "H1czsjtX3h"

    encText = urllib.parse.quote(bookname)
    url = "https://openapi.naver.com/v1/search/book?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))

    else:
        print("Error Code:" + rescode)

    return jsontemp


def navermovie(moviename):

    client_id = "01aH03vjnHWIg5SacVqp"
    client_secret = "H1czsjtX3h"

    encText = urllib.parse.quote(moviename)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))

    else:
        print("Error Code:" + rescode)

    # return jsontemp

def Movieinfo(movieinfo):

    client_id = "01aH03vjnHWIg5SacVqp"
    client_secret = "H1czsjtX3h"

    encText = urllib.parse.quote(movieinfo)
    url = "https://openapi.naver.com/v1/search/movie?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/movie.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        jsontemp = json.loads(response_body.decode('utf-8'))

    else:
        print("Error Code:" + rescode)
    print(jsontemp)
    return jsontemp

# jsonstring = '''
# {"date":"2021-05-11" , "data":[{"price":300 , "total":20},{"price":100 , "total":120}
# ,{"price":1200 , "total":52}]}
# '''
# # 오늘 하루 판매한 토탈 금액
#
# jsonj = json.loads(jsonstring)
# result = jsonj['data']
# # print(result)
# total = 0
# for i in result:
#     # print(i)
#     total = total + (i['price']*i['total'])
# print(total)