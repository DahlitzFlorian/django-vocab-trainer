from django.conf.urls import url
from django.contrib import admin

from . import views


app_name = "vocab"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
]