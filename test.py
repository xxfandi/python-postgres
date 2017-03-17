import cgitb, cgi, datetime, sys, os, json, httplib, hashlib
import cx_Oracle


import sys
sys.path.insert(0, 'C:\Abyss Web Server\htdocs')

import global_variable, global_tryAssign, connectServerAll, tulisFileLog



cgitb.enable()

print "Content-Type: text/html"
print

userdb = global_variable.user_db_web_apps
paswdb = global_variable.pass_db_web_apps
databdb= global_variable.sid_db_web_apps

tryAssign    = global_tryAssign.tryAssign
tryAssign_2D = global_tryAssign.tryAssign_2D
tulis_file   = tulisFileLog.tulis_file

log_filename = 'testPython'
ketFile = '-'
errorSystem = 'Error in system, please contact IT !'
warningException = 'Parameter tidak lengkap'

formatDate2 = {1:'Januari',2:'Februari',3:'Maret',4:'April',5:'Mei',6:'Juni',7:'Juli',8:'Agustus',9:'September',10:'Oktober',11:'November',12:'Desember'}

connect = connectServerAll.cdatabase(str(userdb)+'/'+str(paswdb)+'@'+str(databdb));

form         = cgi.FieldStorage()
try:
	vIp          = cgi.escape(os.environ["REMOTE_ADDR"])
except:
	vIp = ''

def getBrowserIp():
	try:
		import httpagentparser, user_agents

		try:
			vIpS = cgi.escape(os.environ["REMOTE_ADDR"])
		except:
			vIpS = ''

		try:
			vDefaultBrowser = cgi.escape(os.environ.get('HTTP_USER_AGENT','unknown'))
		except:
			vDefaultBrowser = ''

		browser = httpagentparser.simple_detect(vDefaultBrowser)
		browser2 = httpagentparser.detect(vDefaultBrowser) 

		result = {'ip':vIpS, 'default':vDefaultBrowser, 'browser':browser, 'detect':browser2}
		result = {'status': '00', 'msg':'', 'det': result}
	except:
		result = {'status': '01', 'msg':'', 'det': ''}

	return result

def kiriman(vDict):
	result = {'status': '01', 'msg':'', 'det': ''}
	try:
		if(len(vDict) > 0):
			string  = "==";
			for value in vDict:
				string = string+'{'+str(value)+':'+str(vDict[value])+'},'
			string = string+"==";
		else:
			string = '==No Respon==';

		result = {'status': '00', 'msg':'', 'det': string}

	except:
		result['status'] = '01'
		result['msg'] = warningException

	return result


def mainProses():
	ketFile = 'test'
	# vDict = {'versi':'V.2016.1.1', 'nama':'aku'}
	# vGet = kiriman(vDict)

	vGet = getBrowserIp()
	if(vGet['status'] == '00'):
		pesan = vGet['det']
	else :
		pesan = vGet['msg']

	tulis_file(pesan, log_filename, ketFile)
	hasil = json.dumps(pesan)
	return hasil

proses = ''
# proses = mainProses()
try:
	proses = mainProses()
except:
	dictResult = {'status': '02', 'msg':errorSystem, 'det': ''}
	ketFile = 'tryException'
	tulis_file(str(dictResult['status'])+'-'+str(dictResult['msg'])+'##'+str(dictResult['det']), log_filename, ketFile)
	hasil = json.dumps(dictResult)
	proses = hasil

print proses