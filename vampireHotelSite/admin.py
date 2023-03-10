from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ClientOrders)
admin.site.register(ClientReview)