from django.urls import path
#from .views import Surveillant 
from .views import SurveillantViewSet, SalleViewSet, mark_supervisor, FiliereViewSet, NiveauViewSet, UeViewSet, check_supervisor, PlageViewSet, SemestreViewSet, ExamViewSet, ControlerViewSet, ExportAPIView

urlpatterns = [
    path("checksupervisor/<int:id_surv>/", check_supervisor),
    path("marksupervisor/<int:id_present>/", mark_supervisor),
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
    path("horaire" , PlageViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('horaire/<str:pk>', PlageViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path("semestre" , SemestreViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('semestre/<str:pk>', SemestreViewSet.as_view({
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
    path("controle" , ControlerViewSet.as_view({
        "get":"list",
        "post":"create"
    })),
    path('controle/<str:pk>', ControlerViewSet.as_view({
        'get': "retrieve",
        'put': 'update',
        'delete': 'destroy'
    })),
    path('export', ExportAPIView.as_view())
]