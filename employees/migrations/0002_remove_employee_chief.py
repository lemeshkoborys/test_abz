# Generated by Django 2.1.7 on 2019-02-25 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='chief',
        ),
    ]