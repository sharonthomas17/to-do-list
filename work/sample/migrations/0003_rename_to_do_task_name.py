# Generated by Django 3.2 on 2022-08-11 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0002_auto_20220811_0908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='to_do',
            new_name='name',
        ),
    ]