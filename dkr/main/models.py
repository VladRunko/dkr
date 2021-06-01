from django.db import models

class Task(models.Model):
    title = models.CharField('Назва задачі', max_length=40)
    task = models.TextField('Опис задачі')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.id}'


    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачі'

