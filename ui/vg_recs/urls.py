from django.urls import path
from vg_recs import views

urlpatterns = [
    path("", views.home, name="home"),
]