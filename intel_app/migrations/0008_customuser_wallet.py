# Generated by Django 4.1.3 on 2023-08-10 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intel_app', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='wallet',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
