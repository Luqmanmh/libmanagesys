from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Folder(models.Model):
  folder_name = models.CharField(max_length=255)
  parent_folder = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
  
class Book(models.Model):
  Title = models.CharField(max_length=255)
  upload_date = models.DateTimeField(auto_now_add=True)
  parent_folder = models.ForeignKey(Folder, null=True, on_delete=models.CASCADE)
  img = models.ImageField(upload_to='static/previews/', null=True, blank=True)
  writer = models.CharField(max_length=255)
  publisher = models.CharField(max_length=255)
  count = models.CharField(max_length=128)
  synopsis = models.TextField()
  ddc = models.CharField(max_length=10)

