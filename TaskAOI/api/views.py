# Create your views here.
from django.shortcuts import render
from talabaApp.models import Student
# Create your views here.
from homiy.models import Homiy  #modellarimiz
from .serializers import HomiySerializer,TalabaSerializers #serialasers

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView #apiview
from rest_framework import permissions, serializers #ruxsatlar

#permisons tekshiruv
from .permissions import IsAuthorOrReadOnly #file


class Homiylist(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    queryset = Homiy.objects.all()
    serializer_class = HomiySerializer

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)


class HomiyDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Homiy.objects.all()
    serializer_class = HomiySerializer

# User uchun
class TalabaList(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = TalabaSerializers

class TalabaDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = TalabaSerializers



################################################################# Viewsetda ishlash
from rest_framework.viewsets import ModelViewSet
class HomiyViewset(ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Homiy.objects.all()
    serializer_class = HomiySerializer

class TalabaViewset(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = TalabaSerializers