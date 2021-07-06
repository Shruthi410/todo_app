from django.shortcuts import render
from django.utils import timezone
from my_app.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    stuff_for_frontend = {
        "todo_items": todo_items
    }
    return render(request, 'todo_app/index.html', stuff_for_frontend)

def add_todo(request):
    date = timezone.now()
    content = request.POST["content"]
    Todo.objects.create(added_date=date, text=content)
    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
