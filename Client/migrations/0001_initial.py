# Generated by Django 4.0.6 on 2022-08-13 07:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activite', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=25)),
                ('telephone', models.CharField(max_length=25)),
                ('addresse', models.CharField(max_length=25)),
                ('profession', models.CharField(max_length=25)),
                ('num_CIN', models.CharField(max_length=25)),
                ('sexe', models.CharField(choices=[('Masculin', 'Masculin'), ('Féminin', 'Féminin')], max_length=25, null=True)),
                ('lien', models.SlugField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activit', models.CharField(max_length=25)),
                ('tarif', models.PositiveIntegerField()),
                ('date_changement', models.DateField(auto_now_add=True, null=True)),
                ('krk', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_operation', models.DateTimeField(default=datetime.datetime.now)),
                ('nombre', models.PositiveIntegerField(null=True)),
                ('status', models.CharField(choices=[('Payé', 'Payé'), ('Non payé', 'Non payé')], max_length=25, null=True)),
                ('activites', models.ManyToManyField(to='Client.activite')),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Client.client')),
            ],
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateField(auto_now_add=True, null=True)),
                ('fin', models.DateField(auto_now_add=True, null=True)),
                ('date_payement', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Payé', 'Payé'), ('Non payé', 'Non payé')], max_length=25, null=True)),
                ('clients', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Client.client')),
            ],
        ),
    ]
