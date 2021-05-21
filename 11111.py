# -*- coding: utf-8 -*-
import json

과일 = ['바나나','딸기','포도','오렌쥐','레몬']
야채 = ['감자','양파','파~','마늘']


#JSON = Java Script Object Notation

#롯데마트, 이마트, 홈플러스,
#1. 각각 마트별 과일판매
{'마트개수':3,
 '롯데마트':[{'이름':'바나나','가격':500,'원산지':'국내산'}],
 '이마트':[{'이름':'바나나','가격':200,'원산지':'미국산'},{'이름':'오렌지','가격':500,'원산지':'미국산'}],
 '홈플러스':[{'이름':'딸기','가격':1000,'원산지':'국내산'},{'이름':'딸기','가격':3000,'원산지':'국내산'}]
 }

#2. 과일별 분류
{
    '과일개수':3,
    '바나나': [{'가격':500,'원산지':'국내산','판매처':'롯데마트'}],
    '오렌지': [{'가격': 500, '원산지': '국내산', '판매처': '롯데마트'}],
    '딸기': [{'가격': 500, '원산지': '국내산', '판매처': '롯데마트'}]
}

result = {'lastBuildDate': 'Fri, 21 May 2021 10:38:11 +0900', 'total': 74721, 'start': 1, 'display': 10, 'items': [{'title': '삼성전자 <b>비스포크</b> RF85T91S1AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=24395126522', 'image': 'https://shopping-phinf.pstatic.net/main_2439512/24395126522.20201008161501.jpg', 'lprice': '1639000', 'hprice': '', 'mallName': '네이버', 'productId': '24395126522', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RF85T9111T2', 'link': 'https://search.shopping.naver.com/gate.nhn?id=22780234399', 'image': 'https://shopping-phinf.pstatic.net/main_2278023/22780234399.20200715121509.jpg', 'lprice': '1592450', 'hprice': '', 'mallName': '네이버', 'productId': '22780234399', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RF85T9111AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=22680051522', 'image': 'https://shopping-phinf.pstatic.net/main_2268005/22680051522.20200518171924.jpg', 'lprice': '1641950', 'hprice': '', 'mallName': '네이버', 'productId': '22680051522', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RB33T3004AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=23087372490', 'image': 'https://shopping-phinf.pstatic.net/main_2308737/23087372490.20200623122527.jpg', 'lprice': '638820', 'hprice': '', 'mallName': '네이버', 'productId': '23087372490', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '일반형냉장고'}, {'title': '삼성전자 <b>비스포크</b> RF60A91C3AP', 'link': 'https://search.shopping.naver.com/gate.nhn?id=26394480522', 'image': 'https://shopping-phinf.pstatic.net/main_2639448/26394480522.20210317165059.jpg', 'lprice': '1940000', 'hprice': '', 'mallName': '네이버', 'productId': '26394480522', 'productType': '1', 'brand': '비스포크', 'maker': '삼성전자', 'category1': '디지털/가전', 'category2': '주방가전', 'category3': '냉장고', 'category4': '양문형냉장고'}]}

jdata = json.dumps(result)
jdata = json.loads(jdata)

itemsdata = jdata['items']
# print(len(itemsdata))

#2. 제품의 이름만 뽑아서 보고하세요.

# print(result)
titlelist=[]
for i in jdata['items']:
    # print(i['title'])
    titlelist.append(i['title'])
    # print('===========================')
# print(titlelist)


# print(jdata)
#3. 제품의 이름,가격,몰이름을 보고하세요.
alllist=[]
for j in jdata['items']:
    pdict = {}
    pdict['제품명'] = j['title']
    pdict['가격'] = j['lprice']
    pdict['판매몰'] = j['mallName']

    print(pdict)
    alllist.append(pdict)
print(alllist)