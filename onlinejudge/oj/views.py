from django.shortcuts import render
from django.http import HttpResponse, Http404
# Create your views here.

# def home(request):
#     return render(request, 'index.html')

def index(request):
    return render(request, 'oj/ide.html')

def runcode(request):

    if request.method == "POST":
        codeareadata = reqest.POST['codearea']

        try:
            orignal_stdout = sys.stdout
            sys.stdout = open('file.txt' , 'w')

            exec(codeareadata)

            sys.stdout.close()

            sys.stdout = orignal_stdout

            output = open ('file.txt', 'r').read()


        except Exception as e:

            sys.stdout = orignal_stdout

            output = e
    return render(request, 'oj/ide.html', {"code":codearea , "output":output})

