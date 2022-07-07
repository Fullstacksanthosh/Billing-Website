from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.hi,name="homepage"),
    path('login/',views.login,name="loginpage"),
    path('register/',views.register,name="registerpage"),
    path('contact/',views.contact,name="contactpage"),
    path('about/',views.about,name="aboutpage"),
    path('welcome/',views.welcome,name="welcomepage"),
    path('billing/',views.bill,name="billingpage"),
    path('user/',views.user,name="userpage"),
    path('makeorder/',views.makeorder,name="makeorderpage"),
    path('status/',views.status,name="statuspage"),
    path('profile/',views.userprofile,name="userpage"),
    path('admin/',views.adminprofile,name="adminpage"),
    path('adminprofile/',views.adminprofile,name="adminprofilepage"),
]