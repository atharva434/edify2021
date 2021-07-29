# Generated by Django 3.2.3 on 2021-07-29 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edify', '0006_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mathamatics',
            name='link1',
        ),
        migrations.AddField(
            model_name='mathamatics',
            name='channel1',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mathamatics',
            name='channel2',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mathamatics',
            name='channel3',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]