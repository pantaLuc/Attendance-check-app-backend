from django.urls import path
#from .views import Surveillant 
from .views import SurveillantViewSet, SalleViewSet, FiliereViewSet, NiveauViewSet, UeViewSet, ExamViewSet, PresentViewSet

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
    path("faculty" , FiliereViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('faculty/<str:pk>', FiliereViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("niveau" , NiveauViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('niveau/<str:pk>', NiveauViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("matiere" , UeViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('matiere/<str:pk>', UeViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("examen" , ExamViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('examen/<str:pk>', ExamViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("presence" , PresentViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('presence/<str:pk>', PresentViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
]