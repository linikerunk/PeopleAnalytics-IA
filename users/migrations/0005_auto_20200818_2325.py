# Generated by Django 3.1 on 2020-08-19 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200818_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Data de Aniversário'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='resignation',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Demissão'),
        ),
    ]
