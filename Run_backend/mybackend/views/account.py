from django.shortcuts import render
from ..models import Account
from django.core.cache import cache
from ..custombackend import CustomBackend
from django.contrib import messages
from ..serializer import UserSerializer
from django.http import JsonResponse
from django.contrib.auth import logout as auth_logout,login as auth_login
from django.views.decorators.csrf import csrf_exempt
import json

def set_user_cache(user):
    cache.set('user_cache',user)

def get_user_cache():
    return cache.get('user_cache')

@csrf_exempt
def update_all_landmark(request):
    if request.method=='PUT':
        user=get_user_cache()
        data=json.loads(request.body)
        if not isinstance(data,list):
            return JsonResponse({'error':'Bad request'},status=400)
        if user is not None:
            user.all_landmark=data
            user.save()
            set_user_cache(user)
            return JsonResponse({'message':'update landmark'},status=200)
    return JsonResponse({'error':'update landmark failed'},status=400)


@csrf_exempt
def update_information(request):
    if request.method=='PUT':
        user=get_user_cache()
        data=json.loads(request.body)
        if user is not None:
            user.height=data.get('height')
            user.born=data.get('born')
            user.weight=data.get('weight')
            set_user_cache(user)
            user.save()
            return JsonResponse({'message':'update information'},status=200)
    return JsonResponse({'error':'update information failed'},status=400)

@csrf_exempt
def update_spend_time(request):
    if request.method=='PUT':
        data=json.loads(request.body)
        user=get_user_cache()
        if user is not None:
            user.spend_time+=data.get('spend_time')
            user.save()
            set_user_cache(user)
            return JsonResponse({'message':'update spend time'},status=200)
    return JsonResponse({'error':'update spend time failed'},status=400)

@csrf_exempt
def update_distance(request):
    if request.method=='PUT':
        user=get_user_cache()
        data=json.loads(request.body)
        if user is not None:
            user.distance+=data.get('distance')
            user.save()
            set_user_cache(user)
            return JsonResponse({'message':'update distance!'},status=200)
    return JsonResponse({'error':'update distance failed'},status=400)
        

@csrf_exempt
def update_score(request):
    if request.method=='PUT':
        user=get_user_cache()
        data=json.loads(request.body)
        if user is not None:
            user.score=data.get('score')
            user.save()
            set_user_cache(user)
            return JsonResponse({'message':'update score!'},status=200)
    return JsonResponse({'error':'update score failed'},status=400)

@csrf_exempt
def get_account(request):
    if request.method=='GET':
        user=get_user_cache()
        if user is not None:
            serializer=UserSerializer(get_user_cache())
            return JsonResponse(serializer.data,status=200)
        else:
            return JsonResponse({'error':'faile get'},status=400)
    else:
        return JsonResponse({'error':'only get request!'},status=400)

@csrf_exempt
def logout(request):
    if request.method=='GET':
        auth_logout(request)
        set_user_cache(None)
        return JsonResponse({'message':'logout!'},status=200)
    else:
        return JsonResponse({'error':'some error!'},status=400)

    
@csrf_exempt
def login(request):
    if request.method=='POST':
        data=json.loads(request.body)
        username=data.get('username')
        password=data.get('password')
        backend=CustomBackend()
        user=backend.authenticate(request=request,username=username,password=password)
        if user is not None:
            auth_login(request,user,backend='mybackend.custombackend.CustomBackend')
            set_user_cache(user)
            return JsonResponse({'message':'successful login!'},status=200)
        else:
            set_user_cache(None)
            return JsonResponse({'error':'failed login!'},status=401)
    else:
        return JsonResponse({'error':'only use post'},status=400)

@csrf_exempt
def register(request):
    if request.method=='POST':
        data = json.loads(request.body)
        username=data.get('username')
        if Account.objects.filter(username=username).exists():
            return JsonResponse({'error':'username exisits!'},status=400)
        password=data.get('password')
        Account.objects.create_user(username=username,password=password,score=0)
        return JsonResponse({'message':'successful create!'},status=201)
    return JsonResponse({'error':'only POST request'},status=405)


