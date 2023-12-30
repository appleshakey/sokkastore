from django.urls import path
from .views import CreateUser, AuthUser


urlpatterns = [
    path('create_user', CreateUser.as_view()),
    path('auth_user/<str:act>', AuthUser.as_view())
]