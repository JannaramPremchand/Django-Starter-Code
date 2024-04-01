from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signin/', views.sign_in, name='signin'),
    path('signup/', views.sign_up, name='signup'),
]
