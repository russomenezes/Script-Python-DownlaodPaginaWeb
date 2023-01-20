O Objetivo desse scritp é :
*Autenticação no Zabbix
*Acesso a Pagina de Relatório
*Download da Pagina de Relatório 
*Criação de Uma pasta de relatorio 
*Mover arquivos para a pasta 
*Compactação dos arquivos em .zip 
*Exclusão da pastas criada depois da compactação. 
*Envio de Mensagem de Confirmação em grupo no telegram 

Detalhe :

O arquivo  roda apenas com data e hora especifico: 
altere conforme sua necessidade. 



O ambiente  foi criando em maquina linux 
no momento de uso se atente nos links caminho e diretorio  para que funcione no seu ambiente. 
dados para serem alterados em ordem:

1º
browser = webdriver.Firefox(executable_path="SEU CAMINHO PATH/ZabbixScriptRelatorio/geckodriver")

2º
browser.get('http://SEU ZABBIX /index.php')
3º
usuario_input.send_keys('SEU USUARIO')
4º
senha_input.send_keys('SUA SENHA')
5º
browser.get('PAGINA DE RELATORIO ')
6º
	browser123.get('https://api.telegram.org/bot SEU BOOT :KEY SEU BOOT /sendMessage?chat_id=-ID DO SEU GRUPO OU CHAT text=Relatorio%20Zabbix%20Feito✅')

