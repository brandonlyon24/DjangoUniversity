from django.shortcuts import render
from .models import djangoClasses
from . import views
from django.http import HttpResponse



def admin_console(request):
    dejangoClasses = djangoClasses.objects.all()
    return render(request, 'djangoClasses/djangoClasses_page.html', {'djangoClasses': djangoClasses})

