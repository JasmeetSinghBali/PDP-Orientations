from django.shortcuts import render, redirect
from django.http import HttpResponse
# 📝 .models refers to relative import as we are inside the lead app
from .models import Agent, Lead
from .forms import LeadForm, LeadModelForm

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

# using LeadModelForm
def lead_create(request):
    # initially an empty instantiated form
    form = LeadModelForm()
    print(request.POST)
    if request.method == "POST":
        print('Receiving a post request')
        # populate the form with the data filled and grabbed in request.POST
        form = LeadModelForm(request.POST)
        # is_valid makes sure all the data in the form is validated with proper types and so...
        if form.is_valid():
            # 🎯 abstract away all repeated logic automatically saves data from form to db
            form.save()
            # redirects to the leads page showing all leads
            return redirect("/leads")
    context = {
        # 📝: instantiating the form imported from django
        # to pass it as context to create view/route create new Lead
        "form": form
    }
    return render(request, "leads/lead_create.html", context)

# using Simple LeadForm to update new lead
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm()
    print(request.POST)
    if request.method == "POST":
        print('Receiving a post request')
        # populate the form with the data filled and grabbed in request.POST
        form = LeadForm(request.POST)
        # is_valid makes sure all the data in the form is validated with proper types and so...
        if form.is_valid():
            print("form data is valid")
            # cleaned_data is formatted data in dictionary format key:value pairs
            print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            age = form.cleaned_data['age']
            # 🎯update each field for the lead from the form data
            lead.first_name = first_name
            lead.last_name = last_name
            lead.age = age
            lead.save()
            print("The lead was updated.",lead)
            # redirects to the leads page showing all leads
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)


# using Simple LeadForm to create new lead
# def lead_create(request):
#     # initially an empty instantiated form
#     form = LeadForm()
#     print(request.POST)
#     if request.method == "POST":
#         print('Receiving a post request')
#         # populate the form with the data filled and grabbed in request.POST
#         form = LeadForm(request.POST)
#         # is_valid makes sure all the data in the form is validated with proper types and so...
#         if form.is_valid():
#             print("form data is valid")
#             # cleaned_data is formatted data in dictionary format key:value pairs
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             # 📝:objects.first() grabs the forst row in the Agent table
#             agent = Agent.objects.first()
#             # creating a new lead with form data
#             Lead.objects.create(
#                 first_name=first_name,
#                 last_name=last_name,
#                 age=age,
#                 agent=agent
#             )
#             print("A new lead was created.")
#             # redirects to the leads page showing all leads
#             return redirect("/leads")
#     context = {
#         # 📝: instantiating the form imported from django
#         # to pass it as context to create view/route create new Lead
#         "form": form
#     }
#     return render(request, "leads/lead_create.html", context)
