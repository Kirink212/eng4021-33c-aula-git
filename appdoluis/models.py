from django.db import models

class Task(models.Model):
  title = models.CharField(max_length = 50)
  description = models.TextField()
  due_date = models.DateField()
  done = models.BooleanField()
 
class User(models.Model):
  name = models.CharField(max_length = 50)
  email = models.CharField(max_length = 50)
