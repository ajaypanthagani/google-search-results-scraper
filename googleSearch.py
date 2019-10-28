'''
author: ajaypanthagani
language: python 3
pre-requisites:
1. Active internet connection
2. requests library installed
3. BeautifulSoup installed
4. re library installed
5. urllib library installed
'''

#importing all the necessary libraries
import requests
from bs4 import BeautifulSoup
import re
import urllib.parse
from urllib.parse import urlparse
import randomAgent

#defining the googleSearch function
def googleSearch(query):
	#making the url ready for requests
	url = 'https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8'.format(query);
	#generating a random user agent using the randomAgent function we previously defined
	user_agent = randomAgent.getUA()
	#defining header for the request function
	ran_head = {
        	'user-agent': user_agent,
    	}
    #declaring list g_clean to store the fetched urls
	g_clean=[]
	#exception handling code to make sure we don't run into errors
	try:
		#fetching the response using get method in requests
		html = requests.get(url, header=ran_head)
		#checking the response status to be success
		if html.status_code==200:
			#parsing the fetched html in the response using lxml parser in beautiful soup
			soup = BeautifulSoup(html.text, 'lxml')
			#finding all the 'a' tags, links, in the parsed html
			a = soup.find_all('a')
			#looping through the all found a tags for processing
			for i in a:
				#extracting the href attribute for the link to the search results
				k = i.get('href')
				#exception handling code to prevent running into erros
				try:
					#search for the pattern of a url to prevent unneccessary attributes in the result using re module
					m = re.search("(?P<url>https?://[^\s]+)", k)
					#fetching only the url part in the array
					n = m.group(0)
					#splitting the url upto the parameters part to get only the necessary url
					rul = n.split('&')[0]
					#parsing the url to divide it into components using urlparse
					domain = urlparse(rul)
					#checking if the fetched url belongs to google.com if true skip the url
					if(re.search('google.com', domain.netloc)):
						continue
					#else add it to the result list
					else:
						g_clean.append(rul)
				except:
					continue
	except Exception as ex:
		print(str(ex))
	#finally return the result urls
	finally:
		return g_clean 	
