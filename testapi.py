import requests
import json
from Data_api.account_api import accountAPI as api

url = 'http://127.0.0.1:8000/api/'
account=api(url)
#a=account.register('123','456')

account.login('123','456')

result=account.get_account_detail()
score=account.get_score()
landmark={
    'x':100,
    'y':100
}
all_landmark=[]
all_landmark.append(landmark)
account.update_all_landmark(all_landmark)
print(f'\nAccount Detail: \n{result.json()}\n')
print(f'Score: {score}\n')

account.update_score(100)
score=account.get_score()
print(f'New Score: {score}\n')

rank=account.rank()
print(rank.json())
account.logout()
