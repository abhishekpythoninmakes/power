from django.urls import path

from bankapp import views


urlpatterns = [

    path('',views.Home,name='Home'),

]