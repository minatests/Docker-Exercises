# Generated by Django 4.2.3 on 2023-07-14 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogUsers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='dp',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
    ]
