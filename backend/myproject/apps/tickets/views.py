from django.shortcuts import render
from django.http import HttpResponse

def ticket_list(request):
    return HttpResponse("Ticket list")
# Create your views here.
