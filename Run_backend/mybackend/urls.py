from django.urls import path
from . import views

urlpatterns=[
    path('api/login/',views.login),
    path('api/register/',views.register),
    path('api/Account/',views.get_account),
    path('api/logout/',views.logout),
    path('api/score/',views.update_score),
]