# Generated by Django 3.1.3 on 2020-11-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokerApp', '0013_property_rented'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='rented',
            field=models.CharField(blank=True, choices=[('yes', 'yes'), ('no', 'no'), ('ending', 'ending')], default='yes', max_length=10, null=True),
        ),
    ]
