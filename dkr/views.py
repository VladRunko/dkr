from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Task
from .forms import TaskForm
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from json import dumps, loads
from django.conf import settings
import redis
from rest_framework.response import Response
from django.views.generic import DetailView, UpdateView, DeleteView




redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)
redis_access = redis.Redis('localhost', port=6379, db=15)

# redis -> R
def Rget(key):
	return redis_instance.get(key)

def Rput(key,val):
	redis_instance.set(key, val)

def Rdelete(key):
	redis_instance.delete(key)





def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Головна сторінка сайту', 'tasks': tasks})





class TaskDetailView(DetailView):
    model = Task
    template_name = 'main/details_view.html'
    context_object_name = 'article'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'main/create.html'
    form_class = TaskForm
    success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'main/taskdelete.html'
    success_url = '/'





def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма була неправильною'

    form = TaskForm()
    context ={
        'form': form,
        'error': error

    }
    return render(request, 'main/create.html', context)
