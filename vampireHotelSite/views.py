from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

# Create your views here.
def main_view(request):
	return render(request, 'pg1.html', {})

def apartments_view(request):
	booking_form = BookingForm()
	if request.method == "POST":
		booking_form = BookingForm(request.POST)
		if booking_form.is_valid():
			client_data = ClientOrders(**booking_form.cleaned_data)
			client_data.save()
		return HttpResponseRedirect("../")
	context = {
	"form":BookingForm
	}
	return render(request, 'pg2.html', context)

def services_view(request):
	return render(request, 'pg3.html', {})

def gallery_view(request):
	return render(request, 'pg4.html', {})

def reviews_view(request):
	review_form = ReviewForm()
	if request.method == "POST":
		review_form = ReviewForm(request.POST)
		if review_form.is_valid():
			review_data = ClientReview(**review_form.cleaned_data)
			review_data.save()
		return HttpResponseRedirect("../")

	context = {
	"form":review_form
	}
	return render(request, 'pg5.html', context)

def contacts_view(request):
	return render(request, 'pg6.html', {})