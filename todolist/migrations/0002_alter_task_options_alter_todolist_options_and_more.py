# Generated by Django 4.2.10 on 2024-02-06 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'verbose_name': 'Todo List', 'verbose_name_plural': 'Todo Lists'},
        ),
        migrations.AlterField(
            model_name='task',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='todolist.todolist'),
        ),
    ]