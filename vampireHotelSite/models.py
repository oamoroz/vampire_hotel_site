from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ClientOrders(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	age = models.IntegerField()
	gender = models.CharField(max_length=6)
	phone = PhoneNumberField(null=False, blank=False)
	passport_series = models.CharField(max_length=4)
	passport_number = models.CharField(max_length=6)
	arrival_date = models.DateField()
	departure_date = models.DateField()
	apartments_type = models.CharField(max_length=20)
	guests_number = models.IntegerField()

	class Meta:
		verbose_name = 'Client Order'

class ClientReview(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	review = models.CharField(max_length=1500)
	rating = models.IntegerField()