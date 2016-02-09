#!/usr/bin/env python3

import requests

session = requests.Session()
data = {'email': '*', 'password': '*'}
answer = session.post('http://lingualeo.com/ru/login', data)