from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

# Create your views here.

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render_to_response('hospedajes_app/index.html')

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)