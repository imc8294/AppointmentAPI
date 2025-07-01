from datetime import timedelta, datetime
from rest_framework import serializers
from .models import DoctorAvailability, Appointment, DoctorProfile, PatientProfile

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = '__all__'

    def validate(self, data):
        start_time = data['start_time']
        end_time = data['end_time']

        if isinstance(start_time, str):
            start_time = datetime.strptime(start_time, "%H:%M:%S").time()
        if isinstance(end_time, str):
            end_time = datetime.strptime(end_time, "%H:%M:%S").time()


        if start_time >= end_time:
            raise serializers.ValidationError("Start time must be before end time.")

        if data['day_of_week'] not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            raise serializers.ValidationError("Invalid day of the week.")

        
        duration = (datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)).total_seconds() / 60
        if duration not in [15, 30, 45, 60]:
            raise serializers.ValidationError("Availability must be for 15, 30, 45, or 60 minutes.")
        return data
        

class DoctorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorProfile
        fields = '__all__'

        def validate(self, data):
            if data['experience_year'] < 0:
                raise serializers.ValidationError("Experience years can be greater than 0.")
            return data


class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):

        doctor = data['doctor']
        day_of_week = data['day_of_week']
        start_time = data['start_time']
        end_time = data['end_time']

        if isinstance(start_time, str):
            start_time = datetime.strptime(start_time, "%H:%M:%S").time()
        if isinstance(end_time, str):
            end_time = datetime.strptime(end_time, "%H:%M:%S").time()


        if start_time >= end_time:
            raise serializers.ValidationError("Start time must be before end time.")

        if data['day_of_week'] not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            raise serializers.ValidationError("Invalid day of the week.")

        
        duration = (datetime.combine(datetime.today(), end_time) - datetime.combine(datetime.today(), start_time)).total_seconds() / 60
        if duration not in [15, 30, 45, 60]:
            raise serializers.ValidationError("Availability must be for 15, 30, 45, or 60 minutes.")

        availabilities = DoctorAvailability.objects.filter(doctor=doctor, day_of_week=day_of_week)

        valid = any(avail.start_time <= start_time and avail.end_time >= end_time for avail in availabilities)
        if not valid:
            raise serializers.ValidationError("Selected time is outside doctor's availability.")

        # Ensure no overlapping bookings
        overlapping = Appointment.objects.filter(
            doctor=doctor,
            day_of_week=day_of_week,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        if overlapping.exists():
            raise serializers.ValidationError("This time slot is already booked.")
        return data
