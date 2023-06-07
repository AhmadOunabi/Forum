from django.urls import path
from app1 import views as v1


urlpatterns = [
    path('index',v1.index,name='index'),
    path('add',v1.add,name='add'),
]
