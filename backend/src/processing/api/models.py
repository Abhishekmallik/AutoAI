from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
import uuid
from django.utils import timezone

class FileInfo(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username =  models.CharField(max_length=50, blank=False, null=False)
    uploaded_file_name =  models.CharField(max_length=500, default="check",blank=False, null=False)
    processed_file_name =  models.CharField(max_length=500, blank=True, null=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    file_size = models.IntegerField(default=0)

    def __str__(self):
        return (str(self.uploaded_file_name))

class CsvData(models.Model):

    fileinfo = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
    head = models.JSONField(default=list)
    describe = models.JSONField(default=dict)
    missing = models.JSONField(default=dict)
    datatypes = models.JSONField(default=list)
    def __str__(self):
        return str(self.fileinfo.uploaded_file_name)

class ProcessedMetaData(models.Model):

    fileinfo = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
    columns = models.JSONField(default=list)
    actions = models.JSONField(default=dict)
    encoder = models.JSONField(default=dict)
    normalizer = models.JSONField(default=dict)
    def __str__(self):
        return str(self.fileinfo.uploaded_file_name)


class Result(models.Model):

    fileinfo = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
    model = models.CharField(max_length=50, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    parameters = models.JSONField(default=dict)
    metrics = models.JSONField(default=dict)


class Plot(models.Model):

    fileinfo = models.ForeignKey(FileInfo,on_delete=models.CASCADE)
    images = models.ImageField(upload_to='./static/upload/')
    title = models.CharField(max_length=50,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type_of = models.CharField(max_length=50,blank=False,null=False)
