from requests import get
from bs4 import BeautifulSoup as bs

def get_mime(filename):
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

mime_list = download_list()
