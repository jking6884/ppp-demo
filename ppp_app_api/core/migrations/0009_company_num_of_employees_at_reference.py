# Generated by Django 3.1.3 on 2020-11-12 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_company_reference_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='num_of_employees_at_reference',
            field=models.IntegerField(default=110),
            preserve_default=False,
        ),
    ]
