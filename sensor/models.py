from django.db import models

# Create your models here.
class Temperature(models.Model):
	captime=models.DateTimeField(auto_now_add=False)
	captemperature=models.CharField(max_length=10)
	
	def __str__(self):
		return self.captemperature
