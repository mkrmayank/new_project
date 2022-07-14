from django.shortcuts import render

# Create your views here.

def solve(request):
    return render (request, 'oj/question.html')
