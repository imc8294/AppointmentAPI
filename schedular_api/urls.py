from django.urls import path
from .views import AvailabilityListCreate, AvailabilityList, AppointmentListCreate, AppointmentList, DoctorSlot
from .dr_patient_views import DoctorProfileListView, DoctorProfileCreateView, PatientProfileListView, PatientProfileCreateView

urlpatterns = [

    path('doctor/add', DoctorProfileCreateView.as_view()),
    path('doctor', DoctorProfileListView.as_view()),

    path('patient/add', PatientProfileCreateView.as_view()),
    path('patient', PatientProfileListView.as_view()),
    
    path('availability/add', AvailabilityListCreate.as_view()),
    path('availability', AvailabilityList.as_view()),


    path('appointments/add', AppointmentListCreate.as_view()),
    path('appointments', AppointmentList.as_view()),

    path('availability/slot', DoctorSlot.as_view())
]
