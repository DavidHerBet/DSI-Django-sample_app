# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Index page")

def home(request):
	return HttpResponse("<h1>Sample App</h1>")

def help(request):
	return HttpResponse("<h1>Help</h1>")

def about(request):
	return HttpResponse("<h1>About Us</h1>")