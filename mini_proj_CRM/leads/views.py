from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    context = {
        "name": "Joe",
        "age": 34
    }
    #return HttpResponse("Hello world")
    # returning a html page as template when this route is hit
    # render(requestObj, templatenameToRender)
    # 📝now this context can be accessed inside the second_home_page template
    return render(request, "second_home_page.html", context)