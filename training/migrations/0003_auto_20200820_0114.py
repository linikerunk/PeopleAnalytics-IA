# Generated by Django 2.2 on 2020-08-20 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_auto_20200819_2328'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name': 'Entidade', 'verbose_name_plural': 'Entidades'},
        ),
        migrations.RemoveField(
            model_name='entity',
            name='active',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='created',
        ),
        migrations.RemoveField(
            model_name='entity',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='active',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='created',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='modified',
        ),
        migrations.RemoveField(
            model_name='training',
            name='active',
        ),
        migrations.RemoveField(
            model_name='training',
            name='created',
        ),
        migrations.RemoveField(
            model_name='training',
            name='modified',
        ),
        migrations.AddField(
            model_name='event',
            name='entity',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='event', to='training.Entity'),
        ),
        migrations.AddField(
            model_name='event',
            name='instructor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='event', to='training.Instructor'),
        ),
        migrations.AddField(
            model_name='event',
            name='training',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='event', to='training.Training'),
        ),
        migrations.AlterField(
            model_name='training',
            name='workload',
            field=models.CharField(max_length=5, verbose_name='Carga Horária'),
        ),
    ]