from django.shortcuts import render
from django import forms
from django.utils.translation import ugettext as _
from bs4 import BeautifulSoup
from django.shortcuts import redirect
from django.http import JsonResponse
import http.cookies
import urllib.request
import requests
import mysql.connector
import json

cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1',database='cyber_dota')
cursor = cnx.cursor()

i = 0
while i != 56:
	print('id: ' + str(i))
	idh = i
	av = input('Avatar: ')
	text = ''' UPDATE ranks SET avatar = "{}" WHERE id = "{}" '''.format(av, idh) 
	cursor.execute(text)
	cnx.commit()
	i += 1

cnx.close()	
