from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    # return HttpResponse("You did it this time!,")
    return render(request, 'base.html')