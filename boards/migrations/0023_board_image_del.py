# Generated by Django 3.2 on 2023-08-16 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0022_regioncategory_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='image_del',
            field=models.BooleanField(default=False),
        ),
    ]