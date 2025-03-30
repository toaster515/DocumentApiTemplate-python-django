from django.db import models
from enum import Enum

class StorageProvider(models.TextChoices):
    S3 = 'S3'
    AZURE = 'AZURE'

class FileRecord(models.Model):
    id = models.AutoField(db_column="Id",primary_key=True)
    file_name = models.CharField(max_length=255, db_column="FileName")
    provider = models.CharField(max_length=10, choices=StorageProvider.choices, db_column="Provider")
    object_key = models.CharField(max_length=512, db_column="ObjectKey")
    url = models.URLField(db_column="Url")
    uploaded_at = models.DateTimeField(auto_now_add=True, db_column="UploadedAt")

    class Meta:
        db_table = 'file_records'
        app_label = 'documents'