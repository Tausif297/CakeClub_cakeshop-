# Generated by Django 3.2 on 2021-05-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210525_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='register',
            name='r_Phone',
            field=models.CharField(max_length=255),
        ),
    ]
