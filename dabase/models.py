from django.db import models
from django.db.models.deletion import CASCADE
 
"""
Таблица User содержит login, password, firstname, lastname, role

Многие ко многим
"""


class Parent(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    firstname = models.TextField(max_length=100)
    lastname = models.TextField(max_length=100) 

    def __str__(self):
        return self.firstname


class Child(models.Model):
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    firstname = models.TextField(max_length=100)
    lastname = models.TextField(max_length=100)
    parents = models.ManyToManyField(Parent)

    def __str__(self):
        return self.firstname


class Task(models.Model):
    task_text = models.CharField(max_length=200)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True)#, default=Child)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)#, default=Parent)

    def __str__(self):
        return self.task_text
