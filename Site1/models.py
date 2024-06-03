from django.db import models

class Stuff(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"{self.profile_image} {self.firstname} {self.lastname} {self.dob} {self.phone} {self.address}"
    
