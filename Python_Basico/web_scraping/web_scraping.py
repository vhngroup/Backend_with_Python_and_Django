import requests
from bs4 import BeautifulSoup
import urllib
import os.path

def run():
	for i in range(1, 6):
		response = requests.get('https://xkcd.com/{}'.format(i))
		soup = BeautifulSoup(response.content, 'html.parser')
		image_container =soup.find(id='comic')

		image_url = image_container.find('img')['src']
		image_name = image_url.split('/')[-1]
		filepath = file_path = os.path.join('D:\Estudio\Platzi\Python_and_Django\Python_Basico\web_scraping')
		print('Descargando la imagen {} en la carpeta {}'.format(image_name, filepath))
		urllib.request.urlretrieve('https:{}'.format(image_url), filepath)

if __name__ == '__main__':
	run()
