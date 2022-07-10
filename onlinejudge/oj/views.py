from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

# def home(request):
#     return render(request, 'index.html')

def index(request):
    return render(request, 'oj/ide.html')

def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Error!!!")
    return render(request, 'oj/details.html', {'question':question})