from django import forms
from .models import Task, TodoList


class TodolistForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name',)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Project'})


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'due_time', 'priority')

    due_time = forms.DateField(widget=forms.SelectDateWidget)

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Task'})

        self.fields['due_time'].widget.attrs.update(
            {'class': 'input date-input', 'placeholder': 'Due Time', 'type': 'date'})

        self.fields['priority'].widget.attrs.update(
            {'class': 'input', 'placeholder': 'Priority'})
