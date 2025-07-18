from django.db import models
from django.contrib.auth.models import User
from datetime import date
from cloudinary_storage.storage import MediaCloudinaryStorage

class Folder(models.Model):
  folder_name = models.CharField(max_length=255)
  parent_folder = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE)
  
class Book(models.Model):
  Title = models.CharField(max_length=512)
  upload_date = models.DateTimeField(auto_now_add=True)
  parent_folder = models.ForeignKey(Folder, null=True, on_delete=models.CASCADE)
  img = models.ImageField(upload_to='previews/', null=True, blank=True, storage=MediaCloudinaryStorage())
  writer = models.CharField(max_length=255, null=True)
  publisher = models.CharField(max_length=255, null=True)
  count = models.CharField(max_length=128, null=True)
  synopsis = models.TextField(null=True)
  ddc = models.CharField(max_length=10, null=True)

