from django.db import connection
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse
from house.models import Officetels, OneTwoRoom, Villa, Speed, Cafe, Convenience, Culture, Daiso, Fastfood, Health, Hospital, Laundry, Market, NaverPropertyFinal
import psycopg2
import requests
from urllib.parse import urlparse
import re

def latlon(address):
    conn_string = "host='localhost' dbname ='house' user='postgres' password='1111'"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()

    gu = address.split(' ')[1]
    cur.execute(f"SELECT speed FROM SPEED \
            WHERE area='{gu}'") #직장이 속한 구의 대중교통 km/분 평균속도

    gu_speed = cur.fetchall()[0][0] 

    url = "https://dapi.kakao.com/v2/local/search/address.json?&query=" + address
    result = requests.get(urlparse(url).geturl(),
                          headers={"Authorization":"KakaoAK 71dc765801a475a20aec8d82f539dd62"})
    json_obj = result.json()
    global val   # 전역 변수를 지역 범위에서 사용하고 싶을 경우
    for document in json_obj['documents']:
        # 값이 NoneType 일 경우의 오류 방지
        try:
            val = [document['y'], document['x']]
        except:
            val = [0, 0]
    return gu_speed, val # 직장의 위치, 직장의 위도 경도

        
def score(request,input_rent,input_deposit,input_con,gu, job,input_pay,table, data, naver_road):
    print('score')
    num = len(input_con)
    for i in range(num): # 편의시설의 개수만큼 for문 진행 
        if input_con[i] == '병원':
            globals()['con_{}'.format(i)] = 'hos_num'
            globals()['stand_{}'.format(i)] = 5
        elif input_con[i] == '마트':
            globals()['con_{}'.format(i)] = 'mart_num'
            globals()['stand_{}'.format(i)] = 2
        elif input_con[i] == '패스트푸드':
            globals()['con_{}'.format(i)] = 'fast_num'
            globals()['stand_{}'.format(i)] = 2
        elif input_con[i] == '카페':
            globals()['con_{}'.format(i)] = 'cafe_num'
            globals()['stand_{}'.format(i)] = 3
        elif input_con[i] == '문화시설':
            globals()['con_{}'.format(i)] = 'cul_num'
            globals()['stand_{}'.format(i)] = 5
            globals()['table_con_{}'.format(i)] = 'culture'
        elif input_con[i] == '편의점':
            globals()['con_{}'.format(i)] = 'con_num'
            globals()['stand_{}'.format(i)] = 10
        elif input_con[i] == '세탁소':
            globals()['con_{}'.format(i)] = 'laun_num'
            globals()['stand_{}'.format(i)] = 7
        elif input_con[i] == '다이소':
            globals()['con_{}'.format(i)] = 'da_num'
            globals()['stand_{}'.format(i)] = 2
        elif input_con[i] == '실내운동시설':
            globals()['con_{}'.format(i)] = 'gym_num'
            globals()['stand_{}'.format(i)] = 4
    if num == 3:
        solution = data.objects.raw(f"WITH FIRST AS( \
                            SELECT * \
                            FROM \
                                (SELECT gid,address, rent, deposit::integer, pay::integer, road,latitude::float, \
                                longitude::float, area,size,contract, criteria, recent,station_ar, station_na, transfer,\
                            {con_0},{con_1},{con_2}, \
                            (CASE WHEN {con_0} >= {stand_0} THEN 30 ELSE (30 / {stand_0} * {con_0})::float END) AS con0, \
                            (CASE WHEN {con_1} >= {stand_1} THEN 30 ELSE (30 / {stand_1} * {con_1})::float END) AS con1, \
                            (CASE WHEN {con_2} >= {stand_2} THEN 30 ELSE (30 / {stand_2} * {con_2})::float END) AS con2,  \
                            (CASE WHEN station_ar = 2 THEN 50 \
                                    WHEN station_ar = 1 THEN 30 ELSE 10 END) as st1,\
                            (CASE WHEN transfer = 1 THEN 50 ELSE 10 END) as st2, \
                            ST_Distance(geography(ST_MakePoint(longitude, latitude)),  \
                                geography(ST_MakePoint('{job[1]}', '{job[0]}')))/1000 as km \
                                FROM {table} \
                                WHERE rent='{input_rent}' and deposit <= '{input_deposit}' \
                                and pay <= '{input_pay}' and recent = 1) as r) \
                            SELECT gid,address, rent, deposit, pay, latitude, longitude,road, round(size,2) as sizes,contract,criteria, km/{gu} as distance,station_na,\
                            ((con0 + con1 + con2 + 10)/10 + (st1 + st2)/20 + time/10) as score\
                            From (SELECT *, \
                                    (CASE WHEN km/{gu} <= 10 THEN 100 \
                                        WHEN km/{gu} between 10 and 90 THEN (100 - km/{gu}) ELSE 0 END) as time\
                                FROM FIRST) as k \
                            ORDER BY score desc LIMIT 10;") 
    
    elif num == 2:
        solution = data.objects.raw(f"WITH FIRST AS( \
                    SELECT * \
                    FROM \
                        (SELECT gid,address, rent, deposit::integer, pay::integer, latitude::float, road,\
                        longitude::float, size,contract,area, criteria, recent,station_ar, station_na, transfer,\
                       {con_0},{con_1},\
                       (CASE WHEN {con_0} >= {stand_0} THEN 50 ELSE (50 / {stand_0} * {con_0})::float END) AS con0, \
                       (CASE WHEN {con_1} >= {stand_1} THEN 50 ELSE (50 / {stand_1} * {con_1})::float END) AS con1, \
                       (CASE WHEN station_ar = 2 THEN 50 \
                             WHEN station_ar = 1 THEN 30 ELSE 10 END) as st1,\
                       (CASE WHEN transfer = 1 THEN 50 ELSE 10 END) as st2, \
                       ST_Distance(geography(ST_MakePoint(longitude, latitude)),  \
                          geography(ST_MakePoint('{job[1]}', '{job[0]}')))/1000 as km \
                        FROM {table} \
                        WHERE rent='{input_rent}' and deposit <= '{input_deposit}' \
                        and pay <= '{input_pay}' and recent = 1) as r) \
                    SELECT gid,address, rent, deposit, pay, latitude, round(size,2) as sizes,contract,longitude, criteria, road, station_na, km/{gu} as distance,\
                    ((con0 + con1)/10 + (st1 + st2)/20 + time/10) as score\
                    From (SELECT *, \
                            (CASE WHEN km/{gu} <= 10 THEN 100 \
                                  WHEN km/{gu} between 10 and 90 THEN (100 - km/{gu}) ELSE 0 END) as time\
                          FROM FIRST) as k \
                    ORDER BY score desc LIMIT 10;")   

    elif num == 1:
         solution = data.objects.raw(f"WITH FIRST AS( \
                    SELECT * \
                    FROM \
                        (SELECT gid,address, rent, deposit::integer, pay::integer, latitude::float, \
                        longitude::float, area, criteria, size,contract,recent,station_ar, station_na, road,transfer,\
                       {con_0},\
                       (CASE WHEN {con_0} >= {stand_0} THEN 100 ELSE (100 / {stand_0} * {con_0})::float END) AS con0, \
                       (CASE WHEN station_ar = 2 THEN 50 \
                             WHEN station_ar = 1 THEN 30 ELSE 10 END) as st1,\
                       (CASE WHEN transfer = 1 THEN 50 ELSE 10 END) as st2, \
                       ST_Distance(geography(ST_MakePoint(longitude, latitude)),  \
                          geography(ST_MakePoint('{job[1]}', '{job[0]}')))/1000 as km \
                        FROM {table} \
                        WHERE rent='{input_rent}' and deposit <= '{input_deposit}' \
                        and pay <= '{input_pay}' and recent = 1) as r) \
                    SELECT gid,address, rent, deposit, pay, latitude, longitude, round(size,2) as sizes,contract,criteria, station_na, road,km/{gu} as distance,\
                    (con0 /10 + (st1 + st2)/20 + time/10) as score \
                    From (SELECT *, \
                            (CASE WHEN km/{gu} <= 10 THEN 100 \
                                  WHEN km/{gu} between 10 and 90 THEN (100 - km/{gu}) ELSE 0 END) as time\
                          FROM FIRST) as k \
                    ORDER BY score desc LIMIT 10;")       

    else:
        solution = data.objects.raw(f"WITH FIRST AS( \
                    SELECT * \
                    FROM \
                        (SELECT gid,address, rent, deposit::integer, pay::integer, latitude::float, \
                        longitude::float, area,size,contract, criteria, recent,station_ar, station_na, road, transfer,\
                    (CASE WHEN station_ar = 2 THEN 50 \
                            WHEN station_ar = 1 THEN 30 ELSE 10 END) as st1,\
                    (CASE WHEN transfer = 1 THEN 50 ELSE 10 END) as st2, \
                    ST_Distance(geography(ST_MakePoint(longitude, latitude)),  \
                        geography(ST_MakePoint('{job[1]}', '{job[0]}')))/1000 as km \
                        FROM {table} \
                        WHERE rent='{input_rent}' and deposit <= '{input_deposit}' \
                        and pay <= '{input_pay}' and recent = 1) as r) \
                    SELECT gid,address, rent, deposit, pay, latitude, longitude, round(size,2) as sizes,contract,criteria,station_na, road, km/{gu} as distance,\
                    ((st1 + st2)/20 + time/10) as score \
                    From (SELECT *, \
                            (CASE WHEN km/{gu} <= 10 THEN 100 \
                                WHEN km/{gu} between 10 and 90 THEN (100 - km/{gu}) ELSE 0 END) as time\
                        FROM FIRST) as k \
                    ORDER BY score desc LIMIT 10;")
    job_1 = float(job[0])
    job_2 = float(job[1])

    return render(request,'house/solution.html', {'solution':solution, 't1':input_con,'job_1':job_1,'job_2':job_2,'naver_road':naver_road})

def detail(request):
    criteria = request.GET['criteria'].split('/')
    tableName = request.GET['tableName']
    NaverRoad = request.GET['NaverRoad']
    road = criteria[1]
    criteria = criteria[0]
    print(criteria, tableName, road, NaverRoad)
    tableName = tableName.strip("[]").split(",")
    print(tableName)
    num = len(tableName)
    if tableName == ['']:
        num = 0
    
    for i in range(num): # 편의시설의 개수만큼 for문 진행\
        place = re.findall(r'"\s*([^"]*?)\s*"', str(tableName))[i][1:-1]
        print(place)
        if place == '병원':
            con_data = 'hospital'
            sub_data = Hospital
        elif place == '마트':
            con_data = 'market'
            sub_data = Market
        elif place == '패스트푸드':
            con_data = 'fastfood'
            sub_data = Fastfood
        elif place == '카페':
            con_data = 'Cafe'
            sub_data = Cafe
        elif place == '문화시설':
            con_data = 'culture'
            sub_data = Culture
        elif place == '편의점':
            con_data = 'convenience'
            sub_data = Convenience
        elif place == '세탁소':
            con_data = 'laundry'
            sub_data = Laundry
        elif place == '다이소':
            con_data = 'daiso'
            sub_data = Daiso
        elif place == '실내운동시설':
            con_data = 'health'
            sub_data = Health
        detail = sub_data.objects.raw(f"SELECT gid, criteria, con_name, con_addres, con_latitu, con_longit \
                FROM {con_data} \
                WHERE criteria = '{criteria}';")
        globals()['detail_{}'.format(i)] = detail
    naver = NaverPropertyFinal.objects.raw(f"SELECT gid, n_address,n_rent,round(n_size,2) as n_sizes,round(n_size_pro,2) as n_size_pros ,n_deposit,n_pay,n_name,n_floor, n_date \
                    FROM naver_property_final \
                    WHERE {NaverRoad} = '{road}';")
    if num == 3:
        print('a')
        return render(request,'house/solution2.html', {'con_detail_0':detail_0, 'con_detail_1':detail_1,'con_detail_2':detail_2, 'naver':naver})
    elif num == 2:
        print('b')
        return render(request,'house/solution2.html', {'con_detail_0':detail_0, 'con_detail_1':detail_1, 'naver':naver})
    elif num == 1:
        print('c')
        return render(request,'house/solution2.html', {'con_detail_0':detail_0, 'naver':naver})
    else:
        return render(request,'house/solution2.html', {'naver':naver})   


def solution(request):
    try:
        table = request.GET['table']
        input_rent = request.GET['input_rent']
        input_deposit = request.GET['q1']
        if request.GET['q2']:
            input_pay = request.GET['q2']
        else:
            input_pay = 0
        input_con = request.GET.getlist('con_input')
        address = request.GET['q3']
        print(table, input_rent, input_pay, input_deposit, input_con, address)

        global data
        print('condition')
        # 집유형에 따라 해당되는 {table} 도출
        if table == 'officetels':
            data = Officetels
            naver_road = 'n_road'
        elif table == 'villa':
            data = Villa
            naver_road = 'n_road'
        elif table == 'one_two_room':
            data = OneTwoRoom
            naver_road = 'n_road_som'
        gu, job = latlon(address)
        return score(request,input_rent,input_deposit,input_con,gu, job,input_pay,table, data, naver_road)
    except:
        return render(request,'home.html')
