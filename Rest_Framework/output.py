import requests

BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    print(data)
    for obj in data:
        if obj['user'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['user']) + '/')
            print(r2.json())
    return data

def create_update():
    new_data = {'user': 2, 'content': "New Update !!"}
    r = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        print(r.json())
        return r.json()
    return r.text

get_list()
create_update()
