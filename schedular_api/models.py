from django.db import models


class DoctorProfile(models.Model):
    id = models.AutoField(primary_key=True)
    doctor_name = models.CharField(max_length=90)
    specialization = models.CharField(max_length=100)
    experience_year = models.PositiveIntegerField()

    def __str__(self):
        return f"Dr. {self.doctor_name}"

class PatientProfile(models.Model):
    id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.patient_name


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    day_of_week = models.CharField(
        max_length=9,
        choices=[(day, day) for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']],
        default='Monday'
    )  
    start_time = models.TimeField()
    end_time = models.TimeField()


class Appointment(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    day_of_week = models.CharField(
        max_length=9,
        choices=[(day, day) for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']],
        default='Monday'
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
