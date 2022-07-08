from turtle import home
from django.urls import path
from .views import lead_list, lead_detail

app_name = "leads"

urlpatterns = [
    path('',lead_list),
    # the pk in the leads will help to dynamically navigate to specific route and show that lead detail
    path('<pk>/',lead_detail)
]