from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.



def index(request):

  return render(request, "first_app/index.html", context={ "okey": "okeay"})

def route_one(request):
  return HttpResponse("<em>hello world</em><p style='color:red;'>Django</p>")