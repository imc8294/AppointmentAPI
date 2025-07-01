from rest_framework import generics
from .models import DoctorAvailability, Appointment
from .serializers import DoctorAvailabilitySerializer, AppointmentSerializer


class AvailabilityListCreate(generics.CreateAPIView):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer


class AvailabilityList(generics.ListAPIView):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer




class AppointmentListCreate(generics.CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class AppointmentList(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
