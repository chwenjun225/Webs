from django.contrib.auth import views as auth_views 
from django.urls import path 
from . import views 

app_name = 'account'

urlpatterns = [
	# previous login url
	# path('login/', views.user_login, name='login'),
	# login urls and logout urls
	path('login/', auth_views.LoginView.as_view(), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
