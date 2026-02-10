import pandas as pd
import requests
import json

api_url = "https://raw.githubusercontent.com/RodrigoEmerson/ETL/main/url_id_JSON.json"

df = pd.read_csv('dadosID.csv')
user_ids = df['UserID'].tolist()
print("IDs do CSV:", user_ids)

response = requests.get(api_url)
if response.status_code == 200:
    all_users = response.json()
    if isinstance(all_users, str):
        all_users = json.loads(all_users)  # 👈 decodifica a string JSON
else:
    raise Exception(f"Erro ao acessar JSON: {response.status_code}")

print("Tipo de all_users:", type(all_users))
print("Conteúdo de all_users:", all_users)


def get_user(user_id):
    for user in all_users:
        if user["id"] == user_id:
            return user
    return None


users = [user for id in user_ids if (user := get_user(id)) is not None]


print("Usuários encontrados:")
print(json.dumps(users, indent=2, ensure_ascii=False))
