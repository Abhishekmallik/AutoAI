# Generated by Django 3.1.4 on 2021-01-27 13:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('uploaded_file_name', models.CharField(default='check', max_length=500)),
                ('processed_file_name', models.CharField(blank=True, max_length=500, null=True)),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
                ('file_size', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('parameters', models.JSONField(default=dict)),
                ('metrics', models.JSONField(default=dict)),
                ('fileinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processing.fileinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedMetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('columns', models.JSONField(default=list)),
                ('actions', models.JSONField(default=dict)),
                ('fileinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processing.fileinfo')),
            ],
        ),
        migrations.CreateModel(
            name='CsvData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.JSONField(default=list)),
                ('describe', models.JSONField(default=dict)),
                ('missing', models.JSONField(default=dict)),
                ('datatypes', models.JSONField(default=list)),
                ('fileinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processing.fileinfo')),
            ],
        ),
    ]
