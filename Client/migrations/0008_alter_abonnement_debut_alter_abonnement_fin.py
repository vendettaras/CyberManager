# Generated by Django 4.0.6 on 2022-08-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0007_remove_abonnement_date_payement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonnement',
            name='debut',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='abonnement',
            name='fin',
            field=models.DateField(null=True),
        ),
    ]
