from selenium import webdriver  
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from datetime import datetime
from time import sleep
import sys
import schedule
import subprocess
import os
import pyautogui
import pyperclip

def zabbix():
#subprocess.run(["clear"])
	browser = webdriver.Firefox(executable_path="/ZabbixScriptRelatorio/geckodriver")
	browser.get('http://zabbix./zabbix/index.php')
	usuario_input = browser.find_element("xpath", '//*[@id="name"]')
	usuario_input.send_keys('SEU.USER')
	# preencher senha
	senha_input = browser.find_element("xpath", "//*[@id='password']")
	senha_input.send_keys('SUASENHA')
	button = browser.find_element("xpath","/html/body/div[1]/main/div[2]/form/ul/li[4]/button").click()
	browser.get('https://zabbix./zabbix/srv_status.php?period=720')
	pyautogui.hotkey('ctrl', 's')
	pyautogui.hotkey('enter')
	sleep(5)
	subprocess.run(["./zabbix.sh"])
	sleep(30)
	browser123 =browser
	browser123.get('https://api.telegram.org/bot12345978:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/sendMessage?chat_id=-1000000000000&text=Relatorio%20Zabbix%20Feito✅')
	sleep(10)
	browser.quit()

def hprogramada():
	horario = (datetime.today().strftime('%d''/''%m''-''%H:%M'))
	
	subprocess.run(["clear"])
	#print (horario)
	print("Aguardando para Gerar Relatório: "+horario)
	sleep(3)
	sys.stdout.flush()
	sys.setrecursionlimit(5000)
	if horario == "19/01-00:01" or horario =="01/02-00:01" or horario =="01/03-00:01" or horario =="01/03-00:01" or horario =="01/04-00:01":
		zabbix()
		sleep(60)
		print ("Registro feito  ás :",horario)
		hprogramada()
	elif  horario == "01/05-00:01" or horario =="01/06-00:01"or horario =="01/07-00:01" or horario =="01/08-00:01" or horario =="01/09-00:01":
		zabbix()
		sleep(60)
		print ("Registro feito  ás :",horario)
		hprogramada()
	elif horario == "01/10-00:01" or horario =="01/11-00:01"or horario =="01/12-00:01":
		zabbix()
		sleep(60)
		print ("Registro feito  ás :",horario)
		hprogramada()

	else:
		pass
schedule.every(1).seconds.do(hprogramada)

while 1:
	schedule.run_pending()
	sleep(1)