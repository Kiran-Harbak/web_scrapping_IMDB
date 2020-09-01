class IMDB:
	def beautifulSoup(self):
		import requests
		from bs4 import BeautifulSoup 
		r=requests.get('https://www.imdb.com/chart/top/')
		soup= BeautifulSoup(r.content,'html.parser')
		ll=soup.find(class_="lister-list")#forecast-list of all-SR-9.4,....
		#tc=ll.find_all(class_="titleColumn")#All titles-SR,GF,..etc
		# sr=tc[0]#SR
		# sr.find('a').get_text()#'The Shawshank Redemption'
		self.mns=[tag.get_text() for tag in ll.select('.titleColumn a')]
		
		self.yrs=[tag.get_text() for tag in ll.select('.titleColumn span')]
		
		self.rtgs=[tag.get_text() for tag in ll.select('.ratingColumn strong')]
		
		print(len(self.mns))
		# print(f'Movies:{mns} \n Years:{yrs} \n Ratings:{rtgs} ')

	def csvFile(self):
		import pandas as pd
		d = {'Movies Name':self.mns,'Years':self.yrs,'Ratings':self.rtgs}
		df = pd.DataFrame(d)
		df.to_csv('C:/Users/Dell/Desktop/PythonBySagarSir/Web Scrapping/IMDB/IMDB.csv')
		df.head()
		print('SUCCESS!')

	def databaseSqlite3(self):
		import sqlite3
		con = sqlite3.connect('C:/Users/Dell/Desktop/PythonBySagarSir/Web Scrapping/IMDB/IMDB.db')
		c=con.cursor()
		c.execute('CREATE TABLE IMDB(Movie_Name text, Years text, Ratings text)')
		for i in range(250):
		    c.execute('INSERT INTO IMDB(Movie_Name, Years, Ratings) values(?,?,?)',(self.mns[i], self.yrs[i], self.rtgs[i]))
		con.commit()

obj=IMDB()
obj.beautifulSoup()
obj.csvFile()
obj.databaseSqlite3()