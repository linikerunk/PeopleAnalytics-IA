# Generated by Django 2.2 on 2020-08-20 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0005_auto_20200820_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='training',
            field=models.ManyToManyField(to='training.Training'),
        ),
    ]