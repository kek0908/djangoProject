from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('test')

def read(request, id):
    return HttpResponse('Read!'+id)

def create(requset):
    return HttpResponse('create!')