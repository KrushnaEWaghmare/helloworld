from django.shortcuts import render

from django.http import HttpResponse
from .models import Drivers
# Create your views here.
def clientsListing(request):
	clientlistings = Drivers.objects.all()
	print("Recived drivers records",len(clientlistings))
	context ={
		'driversList' : clientlistings

	}
	
	return render(request,'clients/clients.html',context)