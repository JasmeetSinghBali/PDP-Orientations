from django.urls import path
from . import views # import views function(request handler) to map the url to it 

# URLConf
# django by default look for urlpatterns variable
urlpatterns = [
    # /playground is already added as prefix in urls.py of warehouse(root appproject) dir
    # passing ref to view function say_hello not invoking it
    path('hello/',views.say_hello)
]