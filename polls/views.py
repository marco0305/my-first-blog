from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_quesion_list': latest_question_list,
    }
    # output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're lookling at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you're voting on question %s." % question_id)
