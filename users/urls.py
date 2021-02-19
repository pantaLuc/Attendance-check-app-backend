from django.urls import path
from .views import signup, users, signin, AuthenticateUSer


urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    path('users', users),
    path('user', AuthenticateUSer.as_view())
]
