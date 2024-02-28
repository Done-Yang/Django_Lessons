
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [ 
    path('', views.home, name='home_page'),
    path('signUp/', views.sigUp, name="signUp_page"),
    path('logIn/', views.logIn, name="logIn_page"),
    path('deshboard/', login_required(views.deshboard, login_url='/logIn'),name='desboard_page'),

    # url systerm
    path('addUser/', views.signUpForm, name='addUser_page'),
    path('useUser/', views.logInForm, name='useUser_page'),
    path('logout/', views.logOut, name='logout')
]