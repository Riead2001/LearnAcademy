# Generated by Django 5.0.2 on 2024-03-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_payment_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='is_1preview',
            field=models.BooleanField(default=False),
        ),
    ]
