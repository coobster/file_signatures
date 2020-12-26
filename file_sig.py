##########################################
# Check mime types from the file signature bits located 
# at the start of this file rather than parsing the 
# file extension. 
# Requires the requests and Beuatiful Soup libraries to
# retreive the mime_list from wikipedia of a list is not
# provided.
##########################################
from requests import get
from bs4 import BeautifulSoup as bs

def get_mime(filename, mime_list = download_list()):
	##############################################
	#  get_mime function opens and checks the file given and 
	#  checks it for matches from the mime_list given.
	#  If a mime_list is not specified this function will 
	#  run the download_list function and attempt to get
	#  the current list from the wikipedia on file signatures
	###############################################
	data = open(filename,'r+b').read(32)
	for m in mime_list:
		if type(m[0]) == list:
			for i in m[0]:
				if data.hex().upper()[:len(i[0].upper())] == i.upper():
					return m[4]
		else:
			if data.hex().upper()[:len(m[0].upper())] == m[0].upper():
				return m[4]
	return None

def download_list():
	###############################################
	#  download_list funtion returns a list with all the 
	#  known mimetypes from the wikipedia page about file_signatures
	#	https://en.wikipedia.org/wiki/List_of_file_signatures
	#  May not work if wikipedia changes the style of
	#  the webpage (however unlikely that is to occur).
	###############################################
	url = 'https://en.wikipedia.org/wiki/List_of_file_signatures'
	r = get(url)
	soup = bs(r.content)
	mime = [[td.text.strip('\n') for td in tr.findAll('td')] for tr in soup.table.findAll('tr')]
	mime = [i for i in mime if i]
	for i in range(len(mime)):
		mime[i][0] = mime[i][0].replace(' ','')
		if '\n' in mime[i][0]:
			mime[i][0] = [o for o in mime[i][0].split('\n') if o]
	return mime
