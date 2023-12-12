from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def reservation(request):
#     return HttpResponse("Thank you for your reservation")


def index (request):
    return render (request, 'index.html', {})