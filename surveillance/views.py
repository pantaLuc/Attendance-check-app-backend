from django.db.models import Q
import datetime
from django.shortcuts import render
from .models import Surveillant, Salle, Filiere, Niveau, Ue, Plage, Semestre, Exam, Controler
from rest_framework.response import Response
from .serializers import SurveillantSerializer, SalleSerializer, FiliereSerializer, NiveauSerializer, UeSerializer, PlageSerializer, SemestreSerializer, ExamSerializer, ControlerSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.authentication import JwtAuthenticatedUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET'])
@authentication_classes([JwtAuthenticatedUser])
@permission_classes([IsAuthenticated])
def mark_supervisor(request, id_present):
    try:
        supervisor = Controler.objects.get(pk=id_present)
        supervisor.is_present = True
        supervisor.save()
        
        all_presence = Controler.objects.filter(examen=supervisor.examen, salle=supervisor.salle)
        
        for present in all_presence:
            present.user = request.user
            present.save()
        
        return Response({
                        'id_exam': supervisor.id,
                        'surv' : {
                                    "id" : supervisor.surveillant.pk,
                                    "name" : supervisor.surveillant.first_name +" "+supervisor.surveillant.last_name,
                                    "presence" : supervisor.is_present
                                }
                    })
    except Surveillant.DoesNotExist:
        return Response({"message":"Impossible de marquer la presence"})

@api_view(['GET'])
@authentication_classes([JwtAuthenticatedUser])
@permission_classes([IsAuthenticated])
def check_supervisor(request, id_surv):
    try:
        supervisor = Surveillant.objects.get(pk=id_surv)
        
        if supervisor is not None:
            current_time = datetime.datetime.now().time()
            current_date = datetime.datetime.now().date()
            try:
                    
                present = Controler.objects.get(
                                    Q(examen__day=current_date) &
                                    Q(examen__plage__begin__lt=current_time) &
                                    Q(examen__plage__end__gt=current_time) &
                                    Q(surveillant=supervisor))
        
                if present is not None:
                    return Response({
                        'id_exam': present.id,
                        'surv' : {
                                    "id" : supervisor.pk,
                                    "name" : supervisor.first_name +" "+supervisor.last_name
                                },
                        'niveau' : {
                                    'id' : present.examen.ue.level.id,
                                    'niveau' : present.examen.ue.level.level,
                                    'filiere': present.examen.ue.level.filiere.name,
                                },
                        'salle' : {
                                    'id' : present.salle.id,
                                    'code': present.salle.code,
                                    'localisation': present.salle.localisation
                                },
                        'Ue' : {
                                "id": present.examen.ue.id,
                                "code": present.examen.ue.code,
                                "intitule": present.examen.ue.intitule
                            },
                        'Horaire' : {
                            'id' : present.examen.plage.id,
                            'begin' : present.examen.plage.begin,
                            'end' : present.examen.plage.end
                        },
                    })
            except Controler.DoesNotExist:
                return Response({"message":"surveillant ne doit pas surveiller"})
    except Surveillant.DoesNotExist:
        return Response({"message":"Utilisateur invalide"})
  

class SurveillantViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = SurveillantSerializer(Surveillant.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        surveillant = Surveillant.objects.get(id=pk)
        serializer = SurveillantSerializer(surveillant)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = SurveillantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        surveillant = Surveillant.objects.get(id=pk)
        serializer = SurveillantSerializer(instance=surveillant, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        surveillant = Surveillant.objects.get(id=pk)
        surveillant.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class SalleViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = SalleSerializer(Salle.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        salle = Salle.objects.get(id=pk)
        serializer = SalleSerializer(salle)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = SalleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        salle = Salle.objects.get(id=pk)
        serializer = SalleSerializer(instance=salle, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        salle = Salle.objects.get(id=pk)
        salle.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class FiliereViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = FiliereSerializer(Filiere.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        filiere = Filiere.objects.get(id=pk)
        serializer = FiliereSerializer(filiere)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = FiliereSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        filiere = Filiere.objects.get(id=pk)
        serializer = FiliereSerializer(instance=filiere, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        filiere = Filiere.objects.get(id=pk)
        filiere.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class NiveauViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = NiveauSerializer(Niveau.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        niveau = Niveau.objects.get(id=pk)
        serializer = NiveauSerializer(niveau)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = NiveauSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        niveau = Niveau.objects.get(id=pk)
        serializer = NiveauSerializer(instance=niveau, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        niveau = Niveau.objects.get(id=pk)
        niveau.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class UeViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = UeSerializer(Ue.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        ue = Ue.objects.get(id=pk)
        serializer = UeSerializer(ue)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = UeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        ue = Ue.objects.get(id=pk)
        serializer = UeSerializer(instance=ue, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        ue = Ue.objects.get(id=pk)
        ue.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class PlageViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = PlageSerializer(Plage.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        plage = Plage.objects.get(id=pk)
        serializer = PlageSerializer(plage)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = PlageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        plage = Plage.objects.get(id=pk)
        serializer = PlageSerializer(instance=ue, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        plage = Plage.objects.get(id=pk)
        plage.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class SemestreViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = SemestreSerializer(Semestre.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        semestre = Semestre.objects.get(id=pk)
        serializer = SemestreSerializer(semestre)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = SemestreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        semestre = Semestre.objects.get(id=pk)
        serializer = SemestreSerializer(instance=ue, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        semestre = Semestre.objects.get(id=pk)
        semestre.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ExamViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ExamSerializer(Exam.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        exam = Exam.objects.get(id=pk)
        serializer = ExamSerializer(exam)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ExamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        exam = Exam.objects.get(id=pk)
        serializer = ExamSerializer(instance=exam, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        exam = Exam.objects.get(id=pk)
        exam.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




class ControlerViewSet(viewsets.ViewSet):
    authentication_classes = [JwtAuthenticatedUser]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = ControlerSerializer(Controler.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        controler = Controler.objects.get(id=pk)
        serializer = ControlerSerializer(controler)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        serializer = ControlerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        controler = Controler.objects.get(id=pk)
        serializer = ControlerSerializer(instance=controler, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        controler = Controler.objects.get(id=pk)
        controler.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)