# from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    template = loader.get_template('stories/front/index.html')
    return HttpResponse(template.render(context, request))
