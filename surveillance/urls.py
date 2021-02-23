from django.urls import path
#from .views import Surveillant 
from .views import SurveillantViewSet, SalleViewSet

urlpatterns = [
    path("supervisor" , SurveillantViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('supervisor/<str:pk>', SurveillantViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
     path("room" , SalleViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('room/<str:pk>', SalleViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]