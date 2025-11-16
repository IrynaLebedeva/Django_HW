from django.db import models
from django.db.models import PROTECT

CHOISE_STATUS = [
    ("new", "новая"),
    ('in_progress', 'в процессе'),
    ('pending', 'ожидание'),
    ('blocked', 'заблокирована'),
    ('done', 'выполнена'),
]

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200, unique_for_date="created_at", verbose_name="Название задачи")
    description = models.TextField (verbose_name="Описание задачи")
    categories = models.ManyToManyField(Category, related_name='tasks', verbose_name='Категория задачи')
    status = models.CharField(max_length=15, choices=CHOISE_STATUS, verbose_name="Статус задачи")
    deadline = models.DateTimeField(verbose_name="Дата и время дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название подзадачи")
    description = models.TextField(verbose_name="Описание подзадачи")
    task = models.ForeignKey(Task, on_delete=PROTECT, related_name='subtasks', verbose_name='Основная задача')
    status = models.CharField(max_length=20, choices=CHOISE_STATUS, verbose_name="Статус подзадачи")
    deadline = models.DateTimeField(verbose_name="Дата и время дедлайн")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

