from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Todo List"
        verbose_name_plural = "Todo Lists"

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    LOW = "L"
    MEDIUM = "M"
    HIGH = "H"
    priority_choices = [('', 'Priority'), (LOW, "Low"),
                        (MEDIUM, "Medium"), (HIGH, "High")]

    PENDING = "P"
    INPROGRESS = "I"
    DONE = "D"
    status_choices = [(PENDING, 'Pending'), (INPROGRESS,
                                             "In Progress"), (DONE, "Done")]

    todolist = models.ForeignKey(
        TodoList, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=100)
    due_time = models.DateField()
    priority = models.CharField(
        max_length=1, choices=priority_choices)
    status = models.CharField(
        max_length=1, choices=status_choices, default=PENDING)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self) -> str:
        return self.name
