from django.shortcuts import render
from .models import timetable


# Create your views here.


def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        disc = request.POST['disc']
        deadline = request.POST['deadline']

        detail = timetable(title=title, discription=disc, deadline=deadline)
        detail.save()
        context = {
            'works': timetable.objects.all(),
        }
        return render(request, "index.html", context)
    else:
        context = {
            'works': timetable.objects.all().filter(status=False),
        }
        return render(request, "index.html", context)
