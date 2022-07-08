from django.shortcuts import render
from django.http import HttpResponse
# 📝 .models refers to relative import as we are inside the lead app
from .models import Lead

# Create your views here.
def lead_list(request):
    # where leads is a list of object
    leads = Lead.objects.all()
    context ={
        "leads": leads
    }
    return render(request, "leads/lead_list.html", context)

def lead_detail(request,pk):
    # pk is the route path that can be reffernced to the pk in the leads table
    print(pk)
    lead = Lead.objects.get(id=pk)
    print(lead)
    context = {
        "lead": lead
    }
    return render(request,"leads/lead_detail.html", context)