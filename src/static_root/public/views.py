from django.shortcuts import render


def how_it_works(request):
    return render(request, 'public/how_it_works.html', {})


def home(request):
    return render(request, 'public/home.html', {})
