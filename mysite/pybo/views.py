from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
    # return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")


def index(request):
    return render(request, 'pybo/index.html')

def ko(request):
    return render(request, 'pybo/ko.html')

def ko1(request):
    return render(request, 'pybo/ko1.html')

def survey(request):
    return render(request, 'pybo/survey.html')

# def simple2(request):
#     return render(request, 'pybo/simple2.html')