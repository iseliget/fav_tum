import os
import urllib as urllib
import requests
import time
import random

current_time = int(time.time())

while True:

	r = requests.get('https://api.tumblr.com/v2/blog/YOURNAME/likes?api_key=YOUR_API_KEY&before='+str(current_time))
	streams = r.json()
	liked_posts = streams['response']['liked_posts']

	if len(liked_posts) != 0:
		for post in liked_posts:
			time.sleep(2)
			print "==================================="
			print post['timestamp']
			current_time = post['timestamp'] # update time stamp

			if 'photos' in post:
				for photo in post['photos']:
					try:
						print photo['original_size']['url']
						urllib.urlretrieve(photo['original_size']['url'],'/Users/iseliget/Pictures/tumblrFav/'+ str(random.randint(1,1000)) + photo['original_size']['url'].split('/')[-1])
					except urllib.ContentTooShortError:
						print("DID NOT DOWNLOAD: " + str(photo['original_size']['url']))

			elif 'video_url' in post:
				try:
					print post['video_url']
					urllib.urlretrieve(post['video_url'],'/Users/iseliget/Pictures/tumblrFav/'+ str(random.randint(1,1000)) + post['video_url'].split('/')[-1])
				except urllib.ContentTooShortError:
					print("DID NOT DOWNLOAD: " + str(post['video_url']))
	else:
		break
