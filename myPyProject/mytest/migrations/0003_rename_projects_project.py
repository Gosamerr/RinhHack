# Generated by Django 5.1.2 on 2024-11-11 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mytest', '0002_member_projects_delete_members'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
