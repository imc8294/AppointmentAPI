from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DoctorAvailability, Appointment, DoctorProfile
from .serializers import DoctorAvailabilitySerializer, AppointmentSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime, timedelta


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

class DoctorSlot(APIView):
    serializer_class = DoctorAvailabilitySerializer

    def post(self, request):
        doctor = request.data.get('doctor')
        day_of_week = request.data.get('day_of_week')
        time_slot = int(request.data.get('time_slot'))
        AvailabilityList = DoctorAvailability.objects.filter(doctor=doctor)
        doctor_name = DoctorProfile.objects.get(id=doctor)
        if day_of_week:
            AvailabilityList = DoctorAvailability.objects.filter(doctor=doctor, day_of_week=day_of_week)
        weekly_slot = {}
        data = []
        current_day = ''
        previous_day = ''
        for available in AvailabilityList:
            start_time = datetime.combine(datetime.today(), available.start_time)
            end_time = datetime.combine(datetime.today(), available.end_time)
            diff_time = end_time-start_time
            while_counter = diff_time // timedelta(minutes=time_slot)
            current_day = available.day_of_week
            if current_day != previous_day:
                data = []
            for i in range(0, while_counter):
                slot_end_time = start_time + timedelta(minutes=time_slot)
                data.append(f'{start_time.strftime('%H:%M:%S')}-{slot_end_time.strftime('%H:%M:%S')}')
                weekly_slot.update({available.day_of_week: data})
                start_time = slot_end_time
            previous_day = current_day

        return Response({
            "doctor_name": doctor_name.doctor_name,
            "slots": weekly_slot
        })