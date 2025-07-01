from rest_framework import generics
from .models import DoctorProfile, PatientProfile
from .serializers import DoctorProfileSerializer, PatientProfileSerializer
#from rest_framework.permissions import IsAuthenticated


class DoctorProfileCreateView(generics.CreateAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

class DoctorProfileListView(generics.ListAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer

class PatientProfileCreateView(generics.CreateAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer

class PatientProfileListView(generics.ListAPIView):
    queryset = PatientProfile.objects.all()
    serializer_class = PatientProfileSerializer
