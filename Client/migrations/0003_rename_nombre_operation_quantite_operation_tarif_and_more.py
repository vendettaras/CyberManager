# Generated by Django 4.0.6 on 2022-08-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0002_remove_variation_activit_remove_variation_krk_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='nombre',
            new_name='quantite',
        ),
        migrations.AddField(
            model_name='operation',
            name='tarif',
            field=models.PositiveBigIntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]
