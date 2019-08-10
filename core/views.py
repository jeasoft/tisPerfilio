from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EducationSerializer, UserSerializer, ExperienceSerializer, CertificationSerializer
from core.models import User, Experience, Education, Certification

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExperienceViewSet(viewsets.ModelViewSet):

    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):

    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class CertificationViewSet(viewsets.ModelViewSet):

    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer