from django.http import HttpResponse
from django.shortcuts import render


def about(reguest):
	return HttpResponse('Thi is about page !')

def home(reguest):
	return render(reguest, 'home.html', {'greeting': ' Hello!'})

