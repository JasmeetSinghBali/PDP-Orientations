from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    #return HttpResponse("Hello world")
    # returning a html page as template when this route is hit
    # render(requestObj, templatenameToRender)
    return render(request, "second_home_page.html")