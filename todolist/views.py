from typing import Any
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import DeleteView
from django.urls import reverse, reverse_lazy
from . models import TodoList, Task
from . forms import TodolistForm, TaskForm


# Create your views here.
class TodoListView(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        view = TodoListGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        view = TodoListPost.as_view()
        return view(request, *args, **kwargs)


class TodoListGet(ListView):
    model = TodoList
    template_name = "todo/todolists.html"
    context_object_name = 'todolists'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = TodolistForm()
        return context


class TodoListPost(SingleObjectMixin, FormView):
    model = TodoList
    form_class = TodolistForm
    template_name = "todo/todolists.html"
    context_object_name = 'todolists'

    def form_valid(self, form):
        todolist = form.save(commit=False)
        todolist.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('projects')


class TodoListDetailView(View):
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        view = TasksGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        view = TaskPost.as_view()
        return view(request, *args, **kwargs)


class TasksGet(DetailView):
    model = TodoList
    template_name = "todo/todolist.html"
    context_object_name = "todolist"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForm
        return context


class TaskPost(SingleObjectMixin, FormView):
    model = TodoList
    form_class = TaskForm
    template_name = "todo/todolist.html"
    context_object_name = "todolist"

    def form_valid(self, form: Any) -> HttpResponse:
        task = form.save(commit=False)
        task.todolist = self.get_object()
        task.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        proj = self.get_object()
        return reverse('project', kwargs={"pk": proj.pk})


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self) -> str:
        task = self.get_object()
        proj = task.todolist
        return reverse('project', kwargs={'pk': proj.pk})


class ProjectDeleteView(DeleteView):
    model = TodoList

    def get_success_url(self) -> str:
        return reverse('projects')


def next_state(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.status == 'P':
        task.status = 'I'
    elif task.status == 'I':
        task.status = 'D'
    elif task.status == 'D':
        task.status = 'P'
    task.save()

    return redirect('project', task.todolist.pk)
