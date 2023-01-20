#!/bin/bash

# Verificacao se servico esta online
variavel1='RelatorioZabbix-' variavel2=$(date +%F) zabbix=$variavel1$variavel2 
mkdir -p /Downloads/$zabbix
sleep 5
mv /Downloads/LNXZA* /home/cesar/Downloads/$zabbix/
sleep 5
zip -r /Downloads/$zabbix.zip  /Downloads/$zabbix/
sleep 5
cd /Downloads/ 
sleep 30
rm -rf $zabbix/