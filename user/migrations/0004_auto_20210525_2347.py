# Generated by Django 3.2 on 2021-05-25 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_user_register_register'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='Email',
            new_name='r_Email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Password',
            new_name='r_Password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Phone',
            new_name='r_Phone',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='Name',
            new_name='r_name',
        ),
    ]