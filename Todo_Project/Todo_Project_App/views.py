from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .form import TodoForms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Class based View

class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'val'  #---> key name that stores the model objects


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('task', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetails', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def TodoTask(request):
    if request.method == "POST":
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(task=name, priority=priority, date=date)
        task.save()
    tasks = Task.objects.all()
    return render(request, 'index.html', {'val': tasks})


# def details(request):
#     return render(request, 'details.html')

def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def edit(request, id):
    task = Task.objects.get(id=id)
    f = TodoForms(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task, 'form': f})
