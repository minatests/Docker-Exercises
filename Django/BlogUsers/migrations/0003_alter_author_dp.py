# Generated by Django 4.2.3 on 2023-07-14 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogUsers', '0002_author_dp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='dp',
            field=models.ImageField(default='media/images/profile-icon-design-free-vector_9vWQwhV.jpg', upload_to='media/images'),
        ),
    ]