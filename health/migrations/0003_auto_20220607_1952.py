# Generated by Django 3.1.3 on 2022-06-07 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_symptoms_usersymptoms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersymptoms',
            name='my_symptoms',
        ),
        migrations.RemoveField(
            model_name='usersymptoms',
            name='user',
        ),
        migrations.DeleteModel(
            name='symptoms',
        ),
        migrations.DeleteModel(
            name='Usersymptoms',
        ),
    ]
