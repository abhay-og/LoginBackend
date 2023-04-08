from django.urls import path, include
from account.views import *

urlpatterns = [
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(),name="login")
]