from flask import Blueprint, render_template, url_for, request, jsonify
from werkzeug.utils import redirect
from pybo.weatherapi import get_wdata
from pybo.naverapi import navermovie
from pybo.navermovie import get_movie

bp = Blueprint('kakao', __name__, url_prefix='/kakaotalk')

@bp.route('/weather/', methods=('GET','POST'))
def Kakaoweather():
    req = request.get_json()

    print(req)
    if req['intent']['name'] == '날씨 지역 블럭':
        print(req['action']['params']['sys_location'])
        result = get_wdata(req['action']['params']['sys_location'])

        imgurl = '맑음 이미지 주소'
        if result['현재일기'] == "":
            imgurl = ''
        elif result['현재일기'] == "구름":
            imgurl = ''

    elif req['intent']['name'] == '영화 정보 블럭':
        result = navermovie("미나리")
        print(result)





    res = {
        "version":"2.0",
        "template":{
            "outputs":[
                {
                   "simpleText" : {"text":result['현재일기']}
                },
                {
                    "simpleImage": {
                        "imageUrl": imgurl,
                        "altText": result['현재일기']
                    }
                }
            ]
        }
    }

    print(res)

    return jsonify(res)


@bp.route('/movie/', methods=('GET','POST'))
def Kakaomovie():
    result = get_movie()

    moviedata1 = navermovie(result[0][0])
    moviedata2 = navermovie(result[1][0])
    moviedata3 = navermovie(result[2][0])


    print(moviedata1['items'][0]['title'])
    print(moviedata1['items'][0]['subtitle'])
    print(moviedata1['items'][0]['image'])
    print(moviedata1['items'][0]['link'])

    print(result[0][0])

    res = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "listCard": {
                  "header": {
                    "title": "추천영화"
                  },
                  "items": [
                    {
                      "title": moviedata1['items'][0]['title'],
                      "description": moviedata1['items'][0]['subtitle'],
                      "imageUrl": moviedata1['items'][0]['image'],
                      "link": {
                        "web": moviedata1['items'][0]['link']
                      }
                    },
                    {
                      "title": moviedata2['items'][0]['title'],
                      "description": moviedata2['items'][0]['subtitle'],
                      "imageUrl":moviedata2['items'][0]['image'] ,
                      "link": {
                        "web": moviedata2['items'][0]['link']
                      }
                    },
                    {
                      "title": moviedata3['items'][0]['title'],
                      "description": moviedata3['items'][0]['subtitle'],
                      "imageUrl": moviedata3['items'][0]['image'],
                      "link": {
                        "web": moviedata3['items'][0]['link']
                      }
                    }
                  ],
                  "buttons": [
                    {
                      "label": "구경가기",
                      "action": "webLink",
                      "webLinkUrl": "https://namu.wiki/w/%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88"
                    }
                  ]
                }
              }
            ]
          }
        }
    return jsonify(res)