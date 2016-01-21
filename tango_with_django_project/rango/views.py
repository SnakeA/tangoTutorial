from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext



def index(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('index.html', context_dict, context)

def about(request):
    context = RequestContext(request)
    context_dict = {}
    return render_to_response('about.html', context_dict, context)