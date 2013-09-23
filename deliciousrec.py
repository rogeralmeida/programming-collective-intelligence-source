from pydelicious import get_popular,get_userposts,get_urlposts
from time import *

def initializeUserDict(tag,count=5):
	user_dict={}
	for p1 in get_popular(tag=tag)[0:count]:
		for p2 in get_urlposts(p1['url']):
			user=p2['user']
			user_dict[user]={}
	return user_dict

def fillItems(user_dict):
	all_items={}
	for user in user_dict:
		for i in range(3):
			try:
				print "Tentando a "+i+"ª vez pegar os posts do usuario "+user
				posts=get_userposts(user)
				print "Consegui obter os posts do usuario "+user
				print posts
				break
			except Exception as inst:
				print "Failed user "+user+" retrying"
				sleep(4)
		for post in posts:
			url=post['url']
			user_dict[user][url]=1.0
			all_items[url]=1

	for ratings in user_dict.values():
		for item in all_items:
			if item not in ratings:
				ratings[item]=0.0