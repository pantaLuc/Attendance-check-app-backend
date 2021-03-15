from django.urls import path
from .views import (signup, users, signin, AuthenticateUSer,
                    signout, PermissionViewSet, RoleViewSet, UserViewSet
                    )


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
    path('users/info', ProfileUseAPIView.as_view()),
    path('users/password', ProfilePasswordAPIView.as_view()),

    path('roles', RoleViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('role/<str:pk>', RoleViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
<<<<<<< HEAD
    }))
   
=======
    })),
    # path('users', UserGenericAPIVIEW.as_view()),
    # path('users/<str:pk>', UserGenericAPIVIEW.as_view())
    path('users', UserViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('users/<str:pk>', UserViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete'
    }))
>>>>>>> b122a98b6b9052fabf4916e8c5a37a120e09193c
]
