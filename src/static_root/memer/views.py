from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required()
def task_list(request):
    return render(request, 'memer/list.html', {})


@login_required()
def detail(request):
    return render(request, 'memer/detail.html', {})
    

@login_required()
def dashboard(request):
    return render(request, 'memer/dashboard.html', {})
