#!/usr/bin/python

import requests
import json
import time

#clean code

#array python

#regex python

while True:
	time.sleep (25)
	arquivo = open('/home/znt/scrips/log.txt', 'r')
	for linha in arquivo:
	   	print(linha)
	arquivo.close()

	payload = {'entry.722472479': linha}

	r = requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSdPA5fhRbhgxWwNyNUdY7HcuK02kHyuT2IPwBy4kEuyvHn05w/formResponse", data=payload) #2

	print(r.status_code)
	print("Requests SucessFully!\n")
