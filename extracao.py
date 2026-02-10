import pandas as pd
import requests
import json

api_url = "Github"

df = pd.read_csv('dadosID.csv')
user_ids = df['UserID'].tolist()
#print(users_ids)
responde = requests.get(f'{api_url}/{id}')

print(responde)

def get_user(id):
    responde = requests.get(f'{api_url}/id/{id}')
    return responde.json() if responde.status_code == 200 else None

#id = [user for id in user_ids if (user := get_user(id)) is not None]

print(get_user(1))