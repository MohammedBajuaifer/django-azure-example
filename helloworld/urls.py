from django.urls import path

from helloworld import views


urlpatterns = [
    path('index/', views.index, name='index'),
]