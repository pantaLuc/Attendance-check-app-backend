from django.urls import path
from .views import signup, users, signin


urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    path('users', users)
]
