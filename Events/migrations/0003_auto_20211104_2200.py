# Generated by Django 3.2.7 on 2021-11-04 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20211104_1644'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ApplyCandidatesModel',
            new_name='ApplyCandidates',
        ),
        migrations.RenameModel(
            old_name='EmailSubscriberFormModel',
            new_name='EmailSubscriberForm',
        ),
    ]
