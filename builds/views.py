from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone as tz
from builds.models import Build
from .forms import BuildForm
from markdownx.utils import markdownify

# Create your views here.


def index(request):
    builds = Build.objects.order_by('-build_last_edit_date')[:5]
    now = tz.now()
    context = {"now": now,
               "builds": builds,
               }
    return render(request, 'builds/index.html', context)


def view_build(request, pk):
    build = get_object_or_404(Build, pk=pk)
    build.build_usage = markdownify(build.build_usage)
    context = {"build": build}
    return render(request, 'builds/build.html', context)


def create_build(request):
    if request.method == "POST":
        form = BuildForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = BuildForm()
    return render(request, 'builds/new.html', {'form': f'{form}'})
