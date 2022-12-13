from django.urls import re_path as url
from blog import views2

urlpatterns = [
    url(r'strokes', views2.stroke_get)
]
