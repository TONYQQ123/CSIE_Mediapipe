import requests
import json
from .abstract import base_account

class accountAPI(base_account):
    def __init__(self,url):
        self.url=url
    
    def update_information(self,idata):
        url=self.url+'information/'
        information=idata
        data={
            'height':information.get('height'),
            'weight':information.get('weight'),
            'born':information.get('born')
        }
        print(url)
        print(data)
        response=requests.put(url=url,json=data)
        print(response)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
        return response

    def update_spend_time(self,stime):
        url=self.url+'spend_time/'
        data={
            'spend_time':stime
        }
        response=requests.put(url=url,json=data)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
        return response
    
    def update_distance(self,distance):
        url=self.url+'distance/'
        data={
            'distance':distance
        }
        response=requests.put(url=url,json=data)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
        return response

    
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
        return response
    
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
        return response

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
        return response
    
    def logout(self):
        url=self.url+'logout/'
        response=requests.get(url=url)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
        return response
    
    def rank(self):
        url=self.url+'rank/'
        response=requests.get(url)
        if response.status_code!=200:
            print(response.json().get('error'))
            return None
        else:
            return response
    
    def update_all_landmark(self,data):
        url=self.url+'landmark/'
        response=requests.put(url,json=data)
        if response.status_code==200:
            print(response.json().get('message'))
        else:
            print(response.json().get('error'))
        return response




            