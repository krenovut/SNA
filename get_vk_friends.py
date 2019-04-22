
import requests
import json
from time import sleep
from datetime import datetime


def write_json(data):
    with open('adj_list.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def get_all_friends(id):
    access_token = open("access_token.txt", 'r').read()
    params = {
        'user_id' : id,
        'order' : 'random',
        'name_case' : 'nom',
        'access_token' : access_token,
        'v' : 5.95,
        'count' : 2000
    }

    r = requests.get("https://api.vk.com/method/friends.get", params=params).json()
    
    try:
        friends = r['response']['items']
    except:
        friends = []
    
    return friends



def main():
    start = datetime.now()
    my_id = #your id
    my_friends = get_all_friends(my_id)
    

    adj_list = {}
    for friend in my_friends:
        sleep(1)
        foaf = get_all_friends(friend)
        adj_list[friend] = foaf

    end = datetime.now()
    time = end-start
    # print(str(time))

    write_json(adj_list)







if __name__ == '__main__':
    main()