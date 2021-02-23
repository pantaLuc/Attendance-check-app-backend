from django.shortcuts import render
from .models import Surveillant, Salle
from rest_framework.response import Response
from .serializers import SurveillantSerializer, SalleSerializer
from rest_framework.generics import GenericAPIView
from rest_framework import exceptions, status, generics, mixins, viewsets

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
    # authentication_classes = [JWTauthentication]
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
    # authentication_classes = [JWTauthentication]
    # permission_classes = [IsAuthenticated]

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

