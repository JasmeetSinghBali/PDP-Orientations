from django.shortcuts import render
from django.http import HttpResponse

# Create your views(request handler) here.
def say_hello(request):
    # can be used to retreive data from DB
    # transform data
    # send email
    #return HttpResponse('Hello World')
    # return html from server with name that will be passed to hello.html and rendered their
    return render(request, 'hello.html', {'name':'Jakarta'})