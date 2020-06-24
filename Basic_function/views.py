from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    params = {
        'title':'Basic_function/Index',
        'msg':'これは、サンプルで作ったページです。',
        'goto':'next'
    }
    return render(request, 'Basic_function/index.html', params)

def next(request):
    params = {
        'title':'Basic_function/Next',
        'msg':'これは、もう1つのページです。',
        'goto':'index',
    }
    return render(request, 'Basic_function/index.html', params)