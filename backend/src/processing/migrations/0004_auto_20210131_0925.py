# Generated by Django 3.1.4 on 2021-01-31 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0003_plot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plot',
            name='images',
            field=models.ImageField(upload_to='./static/upload/'),
        ),
    ]