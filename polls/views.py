from django.http import HttpResponse
from django.http.response import Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Question



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = { 'latest_question_list': latest_question_list }
    return render(request, 'polls/index.html', context)

    # Above is a shortcut when you want to load a template!
    # Takes rquest object as its first argument, template name, then dictionary.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

    #Also exists: get_list_or_404(), but USE filt() instead of get()

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
