# Generated by Django 4.0.6 on 2022-08-15 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0006_rename_activites_operation_activite_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonnement',
            name='date_payement',
        ),
    ]
