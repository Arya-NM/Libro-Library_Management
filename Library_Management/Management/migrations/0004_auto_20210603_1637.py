# Generated by Django 3.1.7 on 2021-06-03 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0003_auto_20210602_2019'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IssueBooks',
            new_name='IssueBook',
        ),
        migrations.RenameModel(
            old_name='Librarians',
            new_name='Librarian',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Roll_Numner',
            new_name='Roll_Number',
        ),
    ]
