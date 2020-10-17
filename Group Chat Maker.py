import requests
token = "abc"
headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*'}
groupid = "123"
userid = "123"
while True:
	link = f"https://discord.com/api/v8/channels/{groupid}/recipients/{userid}"
	abc = requests.put(link,headers=headers)
	print(abc.text) #lets you know if it works, this is quite a messy project, coulda made it see if the status code is valid and print("made") etc but it's a short simple script xd
  time.sleep(1) #change this to a high amount to avoid ratelimits or just turn it off to spam create in no time xddd

#https://i.imgur.com/69jIxXk.png make a gc while monitoring the network, find something like this and copy the 2 numbers, 1st is group id, 2nd is user id
