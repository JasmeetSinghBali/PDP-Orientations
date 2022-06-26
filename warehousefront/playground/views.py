from django.shortcuts import render
from django.http import HttpResponse

# Create your views(request handler) here.
def I_am_reqHandler(request):
    # can be used to retreive data from DB
    # transform data
    # send email
    return HttpResponse('Hello World')