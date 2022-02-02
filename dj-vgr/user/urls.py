from django.urls import path
from . import views

#url conf module
urlpatterns = [
    path('hello/', views.say_hello) # urls from settins with user/ are passed here
]