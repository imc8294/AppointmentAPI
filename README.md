# AppointmentAPI

## Setup Instructions

1. Install Python 3.12
2. Install Virtualenv library
   ```bash
   pip install virtualenv
   ```
3. Create Virtual env
   ```bash
   python -m venv aroraAssignmentEnv
   ```
4. Activate Virtual Env 
    For Window
   ```bash
   ./aroraAssignmentEnv/Scripts/activate
   ```
   For Ubuntu
   ```bash
   source ./aroraAssignmentEnv/lib/activate
   ```

5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

- **Add Doctor**: `/api/doctor/add`
- **Doctor List**: `/api/doctor`
- **Add Patient**: `/api/patient/add`
- **Patient List**: `/api/patient`
- **Add Doctor Availability**: `/api/availability/add`
- **Doctor Availability List**: `/api/availability`
- **Book Appointment**: `/api/appointments/add`
- **List of Appointment**: `/api/appointments`
