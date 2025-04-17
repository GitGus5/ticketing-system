from django.shortcuts import render
from django.http import HttpResponse

def user_list(request):
    return HttpResponse("User list")
# Create your views here.
