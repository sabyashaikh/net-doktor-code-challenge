# Generated by Django 4.1 on 2022-08-22 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='customer',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
