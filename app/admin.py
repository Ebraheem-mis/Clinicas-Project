from django.contrib import admin

# Register your models here.
from .models import Doctor, Service, Clinic


class DoctorInline(admin.TabularInline):
  model = Doctor


class ClinicAdmin(admin.ModelAdmin):
  list_display = ('clinic_name', 'clinic_phone', 'clinic_area', 'clinic_location')
  search_fields = ['clinic_name']
  list_filter = ("clinic_area",)

  inlines = [
    DoctorInline,
  ]


class DoctorAdmin(admin.ModelAdmin):
  list_display = ('doctor_name', 'doctor_phone', 'majoring')
  search_fields = ['doctor_name']


class ServiceAdmin(admin.ModelAdmin):
  list_display = ('service_type', 'service_price')


admin.site.register(Clinic, ClinicAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Service, ServiceAdmin)


