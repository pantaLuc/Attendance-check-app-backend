from django.shortcuts import render
from .models import Surveillant, Salle, Filiere, Niveau, Ue, Exam, Present
from rest_framework.response import Response
from .serializers import SurveillantSerializer, SalleSerializer, FiliereSerializer, NiveauSerializer, UeSerializer, ExamSerializer, PresentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from users.authentication import JwtAuthenticatedUser
# from rest_framework_simplejwt.authentication import JWTauthentication
#from .serializers import SurveillantSerializer

# class SurveillantCreateView(CreateAPIView):
#     queryset = Surveillant.objects.all()
#     serializer_class = SurveillantCreateSerializer

#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)

# class SurveillantUpdateView(RetrieveUpdateAPIView):
#     queryset = Surveillant.objects.all()
#     serializer_class = SurveillantCreateUpdateSerializer
#     lookup_field = 'phone'
#     lookup_url_kwarg = 'phone'

# class SurveillantGenericAPIVIEW(generics.GenericAPIView,
#                          mixins.ListModelMixin, mixins.RetrieveModelMixin,
#                          mixins.CreateModelMixin, mixins.UpdateModelMixin,
#                          mixins.DestroyModelMixin):
#     queryset = Surveillant.objects.all()
#     serializer_class = SurveillantSerializer

#     def get(self, request, pk=None):
#         if pk:
#             return Response({'data': self.retrieve(request, pk).data})
#         return Response({
#             'data': self.list(request).data
#         })

#     def post(self, request):
#         return Response({
#             "data": self.create(request).data
#         })

#     def put(self, request, pk=None):
#         return Response({
#             "data": self.update(request, pk).data
#         })

#     def delete(self, request, pk=None):
#         return self.destroy(request, pk)


class SurveillantViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

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




class ExamViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

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
        print(request.data)
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




class PresentViewSet(viewsets.ViewSet):
    # authentication_classes = [JwtAuthenticatedUser]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        serializer = PresentSerializer(Present.objects.all(), many=True)
        return Response({
            'data': serializer.data
        })

    def retrieve(self, request, pk=None):
        present = Present.objects.get(id=pk)
        serializer = PresentSerializer(present)
        return Response({
            'data': serializer.data
        })

    def create(self, request):
        print(request.data)
        serializer = PresentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        present = Present.objects.get(id=pk)
        serializer = PresentSerializer(instance=present, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'data': serializer.data}, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        present = Present.objects.get(id=pk)
        present.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


    def present(self, pk=None):
        user = surveillant.objects.get(id=pk)
        if user is None:
            user.is_present = True 
            user.save()
        else:
            user.is_present = False