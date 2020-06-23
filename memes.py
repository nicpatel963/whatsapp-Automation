from bs4 import BeautifulSoup
import requests,random
from lxml import html
def get_memes():
	urls=['https://imgflip.com/tag/trends?sort=latest','https://imgflip.com/tag/trends?sort=latest&after=2yim97','https://imgflip.com/tag/trends?sort=latest&after=2df97a']
	links=[]
	for url in urls:
		data=requests.get(url)
		# scode=html.fromstring(data.content)
		page_soup = BeautifulSoup(data.content, "html.parser")
		divs=page_soup.findAll('div',{'class':'base-unit clearfix'})
		for div in divs:
			try:
				img=div.find('img',{'class':'base-img'})
				# print(img['src'])
				links.append("https:"+img['src'])
			except:
				print("not an imgtype","last img:",links[len(links)-1]," url:",url)


	temp=requests.get(links[random.randint(0,len(links)-1)])
	with open(r'E:\Python\scraping\meme.png','wb')as file:
		file.write(temp.content)
	return r'E:\Python\scraping\meme.png'
if __name__=='__main__':
	print(get_memes())