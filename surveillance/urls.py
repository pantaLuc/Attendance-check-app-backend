from django.urls import path
#from .views import Surveillant 
from .views import SurveillantViewSet

urlpatterns = [
    path("supervisor" ,SurveillantViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('supervisor/<str:pk>', SurveillantViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]