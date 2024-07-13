from django.db import models

class Departments(models.Model):
    dep_name=models.CharField(max_length=100)
    dep_description=models.TextField()

    def __str__(self):
        return self.dep_name
    
class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    doc_image=models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.doc_name
    
class Booking(models.Model):
    person_name=models.CharField(max_length=100)
    person_mobile=models.CharField(max_length=100)
    person_email=models.EmailField(unique=True)
    doc_name=models.CharField(max_length=100)
    booking_date=models.DateTimeField()

    def __str__(self):
        return self.person_name