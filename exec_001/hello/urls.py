from django.conf.urls import url
from .import views

app_name= 'hello'
urlpatterns=[
    url(r'index',views.index,name='index'),
    url(r'about',views.about,name='about'),
    
]