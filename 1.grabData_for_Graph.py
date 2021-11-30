import requests
import json
import time
import os

screen_name="elonmusk" # INPUT Your Username (or any username you want)
directory = "output_friends"
path = './output_friends'
    
# Create the directory 

try: 
    os.mkdir(path) 
except OSError as error:
    print(error)

#Twitter API for getting the data
access_token = "958716870890319872-WajrAitlXmIbxP0QVfmVieIaJk6ZktS"
access_token_secret = "lBtni8TfYcYqFIL9Mhp9RtmmM3QorUq2t9IDJQGAajTS2"
api_key = "DSaamoVhWcE972jRrm5l4GaYE"
api_secret = "m7yLJ00fWzcmBAFigeM73Y4y5XEnYpaJmgCXoFajleeAFZS07g"

r = requests.post('https://api.twitter.com/oauth2/token?grant_type=client_credentials', auth=(api_key,api_secret))
r="AAAAAAAAAAAAAAAAAAAAAM8gPwEAAAAAu89TzADT8Q4PHZ2AyBxIgQMn9OM%3DvqthN4Lg0jOhFEJ2XtHhCUc7ca2YKsZGGTHgtfmnwpFjVHP05Y"


headers = {'Authorization':'Bearer {token}'.format(token=r)}

def download_friends(screen_name,next_cursor):
    friends = []
    max_retry_count = 0

    while(next_cursor != 0 ):
        #you can change "friends" to "followers"
        r = requests.get('https://api.twitter.com/1.1/friends/list.json?cursor={cursor}&screen_name={screen_name}&include_user_entities=true&skip_status=true&count=200'.format(cursor=next_cursor, screen_name=screen_name), headers=headers)
    
        if (r.status_code == 200):
            data = r.json()
            data_friends = [{ "id_str": user["id_str"], "screen_name":user["screen_name"], "friends_count":user["friends_count"]} for user in data["users"]]
            friends.extend(data_friends)

            next_cursor = data["next_cursor"]
            max_retry_count = 0
        elif (r.status_code == 401):
            next_cursor = 0
        else:
            max_retry_count = max_retry_count + 1
            print(r.status_code)
            print(max_retry_count)
            if (max_retry_count >= 20): #Twitter's Limit
                raise Exception('max_retry_count limit reached')
            time.sleep(60)
    
    return friends

#grab the friends
friends = download_friends(screen_name,-1)

with open('./output_friends/{screen_name}.json'.format(screen_name=screen_name), 'w') as file:
    file.write(json.dumps(friends))


for friend in friends:
    screen_name = friend["screen_name"]

    friends_count = friend["friends_count"]
    if (friends_count <= 300):
        indirect_friends = download_friends(screen_name,-1)

        with open('./output_friends/{screen_name}.json'.format(screen_name=screen_name), 'w') as file:
            file.write(json.dumps(indirect_friends))

print("Done, all friends are stored")