# Generated by Django 3.2.24 on 2024-03-23 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_hitcount'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HitCount',
        ),
    ]
