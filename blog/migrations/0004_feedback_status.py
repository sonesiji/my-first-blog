# Generated by Django 3.2.24 on 2024-03-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed')], default='Pending', max_length=20),
        ),
    ]
