from datetime import time
from django.db import models

class Doctor(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    special = models.CharField(max_length=50)
    def __str__(self):
        return self.Name


class Patient(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    mobile = models.IntegerField(null=True)
    address = models.TextField(max_length=50)
    def __str__(self):
        return self.name

class Appoinment(models.Model):
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    # def __str__(self):
    #     return self.Doctor.Name+ "__"+self.Patient.name()
