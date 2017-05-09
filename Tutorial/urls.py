from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(
        r'^home/',
        Home.as_view(),
        name='home'
    ),

]