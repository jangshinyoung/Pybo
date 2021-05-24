from flask import Blueprint, render_template, url_for, request, jsonify
from pybo.models import Question, Answer, Vote
from datetime import datetime
from pybo import db
from werkzeug.utils import redirect
from pybo.movieapi import Mrank
from pybo.naverapi import navermovie,navershop
from pybo.weatherapi import get_wdata

from pybo.models import Userinfo

bp = Blueprint('main',__name__,url_prefix='/')  # 해당 블루프린트로 접근할 url.

# 예) 127.0.0.1:5000/

@bp.route('/test')
def test():
    mrnamelist = ['이찬원', '임영웅', '영탁', '김호중', '정동원', '김희재', '장민호']

    for temp in mrnamelist:
        vote = Vote(mrname = temp, votecount = 0)
        db.session.add(vote)
    db.session.commit()

    return redirect(url_for('main.index'))

@bp.route('/hello')
def hellow_pybo():
    # result = Question.query.filter(Question.id==1).all()
    # result = Question.query.get(1)  # id(primary key)가 1번 데이터 가져옴
    # result = Question.query.filter(Question.subject.like('%무엇%')).all()
    # result = Question.query.filter(Question.username.like('%김%')).all()
    # print(result)
    #
    # result = Question.query.get(1)   # 1번 데이터 가져오기
    # result.subject = '파이보 정말 재밌어요'
    # result = Question.query.get(2)
    # result.subject = '파이보 정말...'
    # result = Question.query.get(3)
    # result.subject = '파이보 재밌어요?'
    # db.session.commit() # commit 적용하기.


    #result= Question.query.get(1)    # 쿼리문 삭제 코드
    #result = Question.query.get(2)
    #db.session.delete(result)
    #db.session.commit()

    #q = Question.query.get(3)    # 쿼리문 답변 넣기 코드
    #a2 = Answer(question=q, content='답변 3번', create_date=datetime.now())
    #db.session.add(a2)
    #db.session.commit()
    q = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고싶습니다.', create_date=datetime.now())
    q1 = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고싶습니다.', create_date=datetime.now())
    q2 = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고싶습니다.', create_date=datetime.now())
    q3 = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고싶습니다.', create_date=datetime.now())
    q4 = Question(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고싶습니다.', create_date=datetime.now())
    #
    db.session.add(q)
    db.session.add(q1)
    db.session.add(q2)
    db.session.add(q3)
    db.session.add(q4)
    db.session.commit()
    # 3번 질문에 대한 답변 데이터를 가져오세요.
    #q = Question.query.get(3)
    #result=q.answer_set
    #print(result)


    #q = Question.query.get(3)
    #db.session.delete(q)
    #db.session.commit()

##############################################################################
    # 5번 질문에 대한 답변을 5개 만드세요.
    #q = Question.query.get(5)
    #a5 = Answer(question=q, content='답변 허허', create_date=datetime.now())
    #db.session.add(a5)
    #db.session.commit()

    # 5번 질문을 역참조하고있는 답변을 출력하세요.
    #q = Question.query.get(5)
    #result=q.answer_set
    #print(result)

    # 5번 질문을 삭제하고 5번 질문을 역참조 하는 답변을 확인하세요.
    #q = Question.query.get(5)
    #db.session.delete(q)
    #db.session.commit()
##############################################################################


############################# 5월 4일 과제 #####################################

    # a1 = Userinfo(user_id='kim', user_pw=123, user_name='김씨', user_age=20, user_add='seoul',
    #               user_sex='man', user_sch='seoul_univer', user_hby='cook', user_date=2002 - 5 - 4,
    #               create_date=datetime.now())
    #
    #
    # a2 = Userinfo(user_id='Gim', user_pw=456, user_name='짐씨', user_age=21, user_add='busan',
    #               user_sex='man', user_sch='busan_univer', user_hby='slip', user_date=2002 - 5 - 5,
    #               create_date=datetime.now())
    #
    #
    # a3 = Userinfo(user_id='Sim', user_pw=789, user_name='심씨', user_age=22, user_add='ulsan',
    #               user_sex='woman', user_sch='ulsan_univer', user_hby='fight', user_date=2002 - 5 - 6,
    #               create_date=datetime.now())
    #
    # a4 = Userinfo(user_id='Bim', user_pw=101112, user_name='빔씨', user_age=23, user_add='pohang',
    #               user_sex='woman', user_sch='pohang_univer', user_hby='swim', user_date=2002 - 5 - 7,
    #               create_date=datetime.now())
    #
    # a5 = Userinfo(user_id='Wim', user_pw=131415, user_name='윔씨', user_age=24, user_add='jinju',
    #               user_sex='man', user_sch='jinju_univer', user_hby='eater', user_date=2002 - 5 - 8,
    #               create_date=datetime.now())
    #
    # a6 = Userinfo(user_id='Xim', user_pw=161718, user_name='씸씨', user_age=25, user_add='sacheon',
    #               user_sex='woman', user_sch='sacheon_univer', user_hby='baseball', user_date=2002 - 5 - 9,
    #               create_date=datetime.now())
    #
    # a7 = Userinfo(user_id='Pim', user_pw=192021, user_name='핌씨', user_age=26, user_add='suwon',
    #               user_sex='woman', user_sch='suwon_univer', user_hby='pingpong', user_date=2002 - 5 - 10,
    #               create_date=datetime.now())
    #
    # a8 = Userinfo(user_id='Aim', user_pw=222324, user_name='아임씨', user_age=27, user_add='incheon',
    #               user_sex='man', user_sch='incheon_univer', user_hby='soccer', user_date=2002 - 5 - 11,
    #               create_date=datetime.now())
    #
    # a9 = Userinfo(user_id='Dim', user_pw=252627, user_name='딤씨', user_age=28, user_add='daejeon',
    #               user_sex='man', user_sch='daejeon_univer', user_hby='singer', user_date=2002 - 5 - 12,
    #               create_date=datetime.now())
    #
    # a10 = Userinfo(user_id='Lim', user_pw=282930, user_name='림씨', user_age=29, user_add='gwangju',
    #                user_sex='woman', user_sch='gwangju_univer', user_hby='dance', user_date=2002 - 5 - 13,
    #                create_date=datetime.now())
    #
    # db.session.add(a1)
    # db.session.add(a2)
    # db.session.add(a3)
    # db.session.add(a4)
    # db.session.add(a5)
    # db.session.add(a6)
    # db.session.add(a7)
    # db.session.add(a8)
    # db.session.add(a9)
    # db.session.add(a10)
    # db.session.commit()

    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))   # 이중 url 바로 연결.

# 네이버 영화, 날씨, 네이버 쇼핑
@bp.route('/webhook',methods=['GET','POST'])
def webhook():
    req = request.get_json()
    # print(req)
    if req['queryResult']['intent']['displayName'] == 'movie ranking':
        rankdata = Mrank()    #movieapi
        result =''
        count = 1
        for temp in rankdata:
            result = result + str(count) + '위 : ' +temp['title']      # 영화 순위 가져오기.
            if count ==3:
                break
            count +=1
    elif req['queryResult']['intent']['displayName'] == 'movie info - custom':

        movieresult = navermovie(req['queryResult']['queryText'])

        moviedata = movieresult['items'][0]


        return movie_info(moviedata['image'],moviedata['title'].replace('<b>', '').replace('</b>',''),moviedata['link'],
                          '감독:'+moviedata['director']+'출연자:'+moviedata['actor'])
    elif req['queryResult']['intent']['displayName'] == 'weather - city':
        wdata = get_wdata(req['queryResult']['queryText'])
        print(wdata)
        return weather_info(wdata)
    elif req['queryResult']['intent']['displayName'] == 'Nshop - custom - custom':
        shopresult = navershop(req['queryResult']['queryText'])
        return shop_info(shopresult['items'])

# 미스터 트롯 투표 dialogflow
@bp.route('/mrvote',methods=['GET','POST'])
def mrvote():
    req = request.get_json()

    if req['queryResult']['intent']['displayName'] == 'trot-member-choice':  # 인텐트 분류:

        votename = req['queryResult']['queryText']

        voteresult = Vote.query.get_or_404(votename)
        print(voteresult.votecount)
        voteresult.votecount += 1
        db.session.commit()

        strdata = votename + "님에게 투표하셨습니다. 이용해주셔서 감사합니다."
        response_json = jsonify(
            fulfillment_text=strdata
        )
        print('===========투표시작===========')

    elif req['queryResult']['intent']['displayName'] == 'trot-rank':  # 미스터 트롯 순위

        question_list = Vote.query.order_by(Vote.votecount.desc())

        strdata = ''
        count = 0
        for temp in question_list:
            count += 1
            strdata = strdata + str(count) + '위 : ' + temp.mrname + "   |   "

        response_json = jsonify(
            fulfillment_text=strdata
        )

    return response_json

@bp.route('/mrtrot')
def mrtrot():
    return render_template('chat/mrtrot.html')

# 다이얼로그 메신저에 이미지 노출
def movie_info(imgurl, title,link,subtitle):
    response_json = jsonify(
        fulfillment_text='영화정보',
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": [[
                        {
                            "type": "image",
                            "rawUrl": imgurl
                        },
                        {
                            "type": "info",
                            "title": title,
                            "actionLink": link,
                            "subtitle": subtitle
                        }
                    ]]
                }
            }
        ]
    )

    print(response_json)
    return response_json   # 영화

# 날씨 정보
def weather_info(wdata):
    strdata = ''

    if '지역' in wdata:
        strdata += wdata['지역']+'의 '
    if '현재일기' in wdata and len(wdata['현재일기'])>1:
        strdata += '현재일기는' + wdata['현재일기']
    if '현재기온' in wdata and len(wdata['현재기온'])>1:
        strdata += '현재기온은' + wdata['현재기온']
    if '일강수' in wdata and len(wdata['일강수'])>1:
        strdata += '일강수는' + wdata['일강수']

    strdata += '입니다.'


    response_json = jsonify(
        fulfillment_text=strdata
    )

    return response_json

# 네이버 샵 정보
def shop_info(items):

    plist = []
    for temp in items:
        imgurl = temp['image']
        title = temp['title']
        link = temp['link']
        subtitle = '최저가 :' + temp['lprice']
        listdata = [
            {
                "type": "image",
                "rawUrl": imgurl
            },
            {
                "type": "info",
                "title": title,
                "actionLink": link,
                "subtitle": subtitle
            }
        ]

        plist.append(listdata)

    response_json = jsonify(
        fulfillment_text=title,
        fulfillment_messages=[
            {
                "payload": {
                    "richContent": plist
                }
            }
        ]
    )

    return response_json


