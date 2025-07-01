# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import User 

# class UserAdmin(BaseUserAdmin):
#     # Display these fields in the user list
#     list_display = ('username', 'email', 'is_doctor', 'is_patient', 'is_staff', 'is_superuser')
    
#     # Add these fields to the user form in admin
#     fieldsets = BaseUserAdmin.fieldsets + (
#         ('Role Info', {'fields': ('is_doctor', 'is_patient')}),
#     )

# admin.site.register(User, UserAdmin)
