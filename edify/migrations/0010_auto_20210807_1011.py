# Generated by Django 3.2.3 on 2021-08-07 04:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('edify', '0009_rename_desc_contact_suggestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='suggestions',
        ),
        migrations.AddField(
            model_name='contact',
            name='remarks',
            field=models.TextField(default=django.utils.timezone.now, help_text='we are at 99% what would u say to make it perfect'),
            preserve_default=False,
        ),
    ]
