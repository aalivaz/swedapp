# Generated by Django 2.0.8 on 2018-09-04 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swenglish', '0002_auto_20180904_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordlist',
            old_name='Title',
            new_name='title',
        ),
    ]
