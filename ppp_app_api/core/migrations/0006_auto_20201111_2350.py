# Generated by Django 3.1.3 on 2020-11-11 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201111_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ein',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sba_number',
            field=models.IntegerField(unique=True),
        ),
    ]