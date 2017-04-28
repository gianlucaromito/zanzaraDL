import urllib.request
import logging
import logging.handlers
from datetime import datetime, date, timedelta
import time


#logging, max 2M a file e ne tengo solo 5
LOG_FILENAME = 'log\zanzara_dl.log'
logger = logging.getLogger('zanzara_dl')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=2097152, backupCount=5)
handler.setFormatter(formatter)
logger.addHandler(handler)


debug = 0
if debug == 1:
	data_oggi = date.today() - timedelta(2)
else:
	data_oggi = date.today()
weekday = data_oggi.weekday()
data_oggi = data_oggi.strftime('%y%m%d') # data di oggi formattata in modo da matchare eventualmente con qualcosa 
url = 'http://audio.radio24.ilsole24ore.com/radio24_audio/2017/' + data_oggi + '-lazanzara-s.mp3'

logger.info('l\'url da scaricare è: '+ url)

giorni_sett = {'0':'Lunedì', '1':'Martedì', '2':'Mercoledì', '3':'Giovedì', '4': 'Venerdì', '5': 'Sabato', '6': 'Domenica'}
print('la data è: ' + data_oggi + ' ed è ' + giorni_sett[str(weekday)])


if weekday == 5:
	logger.info('Oggi è ' + giorni_sett[str(weekday)] + ' e quindi non scarico nulla')
	print('Oggi è ' + giorni_sett[str(weekday)] + ' e quindi non scarico nulla')
	exit()
elif weekday == 6:
	logger.info('Oggi è ' + giorni_sett[str(weekday)] + ' e quindi non scarico nulla')
	print('Oggi è ' + giorni_sett[str(weekday)] + ' e quindi non scarico nulla')
	exit()

logger.info('Inizio a scaricare ' + data_oggi + '-lazanzara-s.mp3')
if debug == 0:	
	try:
		urllib.request.urlretrieve(url, 'podcasts/' + data_oggi + '-lazanzara-s.mp3')
	except:
		logger.error('Problemi nello scaricamento del file')	

logger.info('Ho finito di scaricare ' + data_oggi + '-lazanzara-s.mp3')
