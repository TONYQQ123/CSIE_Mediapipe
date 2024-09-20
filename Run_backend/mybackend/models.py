from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

class Account(User):
    score = models.IntegerField(default=0)
    distance = models.FloatField(default=0.0)
    spend_time = models.FloatField(default=0.0)
    born = models.DateTimeField(default=datetime(1970, 1, 1))
    height = models.FloatField(default=170, validators=[MaxValueValidator(250), MinValueValidator(70)])
    weight = models.FloatField(default=70, validators=[MaxValueValidator(300), MinValueValidator(30)])
    all_landmarks=models.JSONField(default=list,null=True)
    video_detail=models.JSONField(default={})
