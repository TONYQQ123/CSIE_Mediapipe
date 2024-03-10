import requests
import json
from .abstract import base_account

class accountAPI(base_account):
    def __init__(self,url):
        self.url=url
    
    def update_score(self,score):
        url=self.url+'score/'
        data={
            "score":score
        }
        response=requests.put(url=url,json=data)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
    
    def get_score(self):
        response=self.get_account_detail()
        if response.status_code==200:
            return response.json().get('score')
        else:
            return None

    def get_account_detail(self):
        url=self.url+'Account/'
        response=requests.get(url=url)
        if response.status_code==400:
            print(response.json().get('error'))
            return None
        elif response.status_code==200:
            return response
    
    def login(self,username,password):
        url=self.url+'login/'
        data={
            "username":username,
            "password":password,
        }
        response=requests.post(url,json=data)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))

    def register(self,username,password):
        url=self.url+'register/'
        data={
            "username":username,
            "password":password,
        }
        response=requests.post(url,json=data)
        if response.status_code==201:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
    
    def logout(self):
        url=self.url+'logout/'
        response=requests.get(url=url)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))


            