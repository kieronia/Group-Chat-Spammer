
import requests
token = "abc"
headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*'}
groupid = "123"   #https://i.imgur.com/fPqUQr5.png copy the number at the top when your in the group to get the ID (use a browser) or with dev tools right click the gc and copy id
userid = "123" #https://i.imgur.com/eJeWUX0.png turn on dev tools, right click a user and copy their ID!
link = f"https://discord.com/api/v8/channels/{groupid}/recipients/{userid}"
while True:
	abc = requests.put(link,headers=headers)
	print(abc.text) #lets you know if it works, this is quite a messy project, coulda made it see if the status code is valid and print("made") etc but it's a short simple script xd
	abc = requests.delete(link,headers=headers)
	print(abc.text)
