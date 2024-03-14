from django.urls import path
import mybackend.views.account as account
import mybackend.views.Start as Start

urlpatterns=[
    path('api/login/',account.login),
    path('api/register/',account.register),
    path('api/Account/',account.get_account),
    path('api/logout/',account.logout),
    path('api/score/',account.update_score),
    path('api/spend_time/',account.update_spend_time),
    path('api/distance/',account.update_distance),
    path('api/information/',account.update_information),
    path('api/rank/',Start.get_rank),
]