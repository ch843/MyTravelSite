from django.shortcuts import render
from django.http import HttpResponse
        
def indexPageView(request) :
    return render(request, 'travelpages/index.html') 
  