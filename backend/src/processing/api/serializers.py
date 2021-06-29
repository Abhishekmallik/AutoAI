from rest_framework import serializers
from django.db import models
from processing.api.models import FileInfo


class FileInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = FileInfo
        fields = ('id','username','uploaded_file_name','processed_file_name')


