import requests
import json
from Data_api.account_api import accountAPI as api

url = 'http://127.0.0.1:8000/api/'
account=api(url)
#a=account.register('123','456')

account.login('123','456')


score=account.get_score()
landmark={
    'x':100,
    'y':100
}
all_landmark=[]
all_landmark.append(landmark)
a=account.update_all_landmark(all_landmark)

print(f'Score: {score}\n')

account.update_score(100)
score=account.get_score()
print(f'New Score: {score}\n')

rank=account.rank()
print(rank.json())

detail={}
detail['test']='Hi!!!!!!!!!!!!'
dt=account.update_video_detail(data=detail)
print(dt)
result=account.get_account_detail()
print(f'\nAccount Detail: \n{result.json()}\n')
account.logout()
