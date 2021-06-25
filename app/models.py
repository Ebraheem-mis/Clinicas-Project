from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patient_email = models.EmailField(max_length=254)
    patient_phone = models.IntegerField()
    patient_area = models.CharField(max_length=50)
    patient_address = models.CharField(max_length=100)


class Clinic(models.Model):
    clinic_name = models.CharField(max_length=50)
    clinic_email = models.EmailField(max_length=254)
    clinic_phone = models.IntegerField()
    clinic_area = models.CharField(max_length=50)
    clinic_address = models.CharField(max_length=100)


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=50)
    majoring = models.CharField(max_length=50)
    clinic_email = models.EmailField(max_length=254)
    clinic_phone = models.IntegerField()
    clinic = models.ForeignKey('Clinic', on_delete=models.CASCADE,)
    


class Appointment(models.Model):

    STATUS = (
      (0,'Schedule'),
      (1,'Confirmed'),
      (2,'Cancelled'),
    )

    appointment_date = models.DateTimeField(auto_now_add=True)
    appointment_status = models.IntegerField(choices=STATUS, default=0)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE,)
    clinic_ap = models.ForeignKey('Clinic', on_delete=models.CASCADE,)



class Payment(models.Model):

    PAYMENT_STATUS = (
      (0,'Unpaid'),
      (1,'Paid'),
      (2,'Failed'),
    ) 

    PAYMENT_METHOD = (
      (0,'Card'),
      (1,'Cash'),
    ) 

    payment_date = models.DateTimeField(auto_now=False)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS, default=0)
    payment_method = models.IntegerField(choices=PAYMENT_METHOD, default=0)
    patient_pay = models.ForeignKey('Patient', on_delete=models.CASCADE,)
    service = models.ForeignKey('Service', on_delete=models.CASCADE,)
    

class Service(models.Model):
    service_type = models.CharField(max_length=50)
    service_price = models.FloatField(default=0)
    

   
    

   

