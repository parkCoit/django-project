from django.urls import re_path as url
from blog import views2

urlpatterns = [
    url(r'stroke', views2.stroke)
]
