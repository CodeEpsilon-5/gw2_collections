from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone as tz
from builds.models import Build

# Create your views here.


def index(request):
    builds = Build.objects.order_by('-build_last_edit_date')[:5]
    now = tz.now()
    context = {"now": now,
               "builds": builds,
               }
    return render(request, 'builds/index.html', context)


def view_build(request, pk):
    build = Build.objects.get(pk=pk)
    context = {"build": build}
    return render(request, 'builds/build.html', context)
