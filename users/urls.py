from django.urls import path
from .views import (signup, users, signin, AuthenticateUSer,
                    signout, PermissionViewSet, RoleViewSet,
                    ProfileUseAPIView, ProfilePasswordAPIView)


urlpatterns = [
    path('signup', signup),
    path('signin', signin),
    path('users', users),
    path('currentuser', AuthenticateUSer.as_view()),
    path('signout', signout),
    path("permissions", PermissionViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('role/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
    })),
    path('users/info', ProfileUseAPIView.as_view()),
    path('users/password', ProfilePasswordAPIView.as_view())

]
