# Generated by Django 3.2.6 on 2021-08-17 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_tdd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
