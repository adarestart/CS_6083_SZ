# Generated by Django 4.0.4 on 2022-05-08 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_alter_vehicleclass_daily_rate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleoffice',
            name='state',
            field=models.CharField(default='NY', max_length=2, verbose_name='state'),
        ),
    ]
