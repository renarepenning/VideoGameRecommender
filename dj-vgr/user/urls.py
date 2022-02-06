from django.urls import path
from . import views

#url conf module
urlpatterns = [
    path('', views.user_home), # urls from settins with user/ are passed here
    # this will query user id
    ## NOT WORKING W NAME RN? THIS  IT NEEDS TO BE ID ATM. TRY WITH 1 OR 2'''
    path('user-query/<str:name>', views.get_name, name="get_name"),

    path('game/<str:gname>', views.game_by_name, name="game_by_name"),
]