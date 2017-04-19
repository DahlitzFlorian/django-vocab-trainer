from django.shortcuts import render


def index(request):

    return render(request, 'vocabtrainer/index.html')