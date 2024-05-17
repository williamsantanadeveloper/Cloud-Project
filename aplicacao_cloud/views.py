from django.shortcuts import render


def index(request):
    print('funcionou')
    return render(request, 'index.html')