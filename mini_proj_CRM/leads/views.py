from django.shortcuts import render
from django.http import HttpResponse
# 📝 .models refers to relative import as we are inside the lead app
from .models import Lead

# Create your views here.
def home_page(request):
    # where leads is a list of object
    leads = Lead.objects.all()
    context ={
        "leads": leads
    }
    #return HttpResponse("Hello world")
    # returning a html page as template when this route is hit
    # render(requestObj, templatenameToRender)
    # 📝now this context can be accessed inside the second_home_page template
    return render(request, "second_home_page.html", context)