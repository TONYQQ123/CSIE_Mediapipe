from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from .models import Account

class CustomBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username, password, **kwargs: Any):
        user=self.custom_auth(username,password)
        if user is not None:
            return user
        return None
    
    def custom_auth(self,username,password):
        user_model=get_user_model()
        try:
            user=Account.objects.get(username=username)
        except user_model.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None