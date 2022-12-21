from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    title  = models.CharField(max_length=50,verbose_name="Tittle :")
    task  = models.TextField(max_length=1000,verbose_name="Task :")
    author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    completed = models.BooleanField(verbose_name="Completed",default=False)
    created = models.DateTimeField( auto_now=False, auto_now_add=True)
    updated = models.DateTimeField( auto_now=True, auto_now_add=False)    

    def __str__(self):
        return self.title

