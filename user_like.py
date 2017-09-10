import random
import os
from urllib.request import urlretrieve
import time
import pytumblr

client = pytumblr.TumblrRestClient(
  secret_str_1,
  secret_str_2,
  secret_str_3,
  secret_str_4
)

client.info()
liked_timestamp = int(time.time())

while True:
	print("=========================================================")

	liked_posts = client.likes(before=liked_timestamp)['liked_posts']

	if len(liked_posts) == 0:
		print(liked_posts)

	if len(liked_posts) != 0:
		for post in liked_posts:
			print("\nType: " + post['type'])

			liked_timestamp = post['liked_timestamp']

			if 'photos' in post:
				for photo in post['photos']:
					try:
						urlretrieve(photo['original_size']['url'],'/Users/username/Pictures/tumblrFav/'+ str(random.randint(1,1000)) + photo['original_size']['url'].split('/')[-1])
						print(str(photo['original_size']['url']))
					except Exception as e:
						print(e)
						print("DID NOT DOWNLOAD: " + str(photo['original_size']['url']))

			elif 'video_url' in post:
				try:
					urlretrieve(post['video_url'],'/Users/username/Pictures/tumblrFav/'+ str(random.randint(1,1000)) + post['video_url'].split('/')[-1])
					print(str(post['video_url']))
				except Exception as e:
					print("DID NOT DOWNLOAD: " + str(post['video_url']))
					print(e)
	else:
		break
