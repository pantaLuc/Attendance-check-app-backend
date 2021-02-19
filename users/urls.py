from django.urls import path
from .views import signup, users, signin, AuthenticateUSer, signout


urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    path('users', users),
    path('currentuser', AuthenticateUSer.as_view()),
    path('signout', signout)
]
