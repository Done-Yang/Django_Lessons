from django.urls import path
from . import views


urlpatterns = [
    path('', views.logIn, name='logIn_page'),
    path('hod/', views.hod, name='hod_page'),
    path('deshboard/', views.deshboard, name='deshboard_page'),
    path('signUp/', views.signUp, name='signUp_page'),
    

    # systerm pattern
    path('addUser/', views.addUser, name='addUser_page'),
    path('logInForm/', views.logInForm, name='logInForm_page'),
    path('logOut/', views.logOut, name='logOut')
]