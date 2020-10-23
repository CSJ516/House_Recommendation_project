from django.db import connection
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.urls import reverse
from house.models import Officetels, OneTwoRoom, Villa, Speed



aa = Officetels
def solution(request):
    input_rent = request.GET['input_rent']
    input_deposit = request.GET['q1']
    input_pay = request.GET['q2']
    job = ['37.5901684571627', '127.05156387144']
    con_0 = 'fast_num'
    con_1 = 'mart_num'
    con_2 = 'cafe_num'
    gu = '0.24069938698647905'
    table = request.GET['table']
    stand_0 = 2
    stand_1 = 2
    stand_2 = 3
    solution = Officetels.objects.raw(f"WITH FIRST AS( \
                        SELECT * \
                        FROM \
                            (SELECT gid,address, rent, deposit::integer, pay::integer, latitude::float, \
                            longitude::float, area, criteria, recent,station_ar, transfer,\
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
                        SELECT gid,address, rent, deposit, pay, latitude, longitude, criteria, km/{gu} as distance,\
                        ((con0 + con1 + con2 + 10)/10 + (st1 + st2)/20 + time/10) as score \
                        From (SELECT *, \
                                (CASE WHEN km/{gu} <= 10 THEN 100 \
                                    WHEN km/{gu} between 10 and 90 THEN (100 - km/{gu}) ELSE 0 END) as time\
                            FROM FIRST) as k \
                        ORDER BY score desc LIMIT 10;")
                        
    return render(request,'house/solution.html', {'solution':solution})