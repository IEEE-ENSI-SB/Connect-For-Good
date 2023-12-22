from django.urls import path
from . import views
urlpatterns = [
    path('', views.Donations, name='Donate'),
    path('feeds/', views.Feeds, name='feeds'),
    path('event/<str:pk>/', views.Post_view, name='Post_view'),
    path('Login/', views.Login_user, name= 'login'),
    path('Register/', views.Register, name= 'register'),
    path('logout/', views.user_logout, name='logout'),
]
