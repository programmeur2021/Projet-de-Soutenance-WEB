# Generated by Django 5.1.2 on 2024-11-27 06:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestionParrainage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle_operation', models.CharField(max_length=100)),
                ('date_operation', models.DateField(auto_now=True)),
                ('montant_debiter', models.DecimalField(decimal_places=2, max_digits=12)),
                ('montant_crediter', models.DecimalField(decimal_places=2, max_digits=12)),
                ('numero_banque', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Caisse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_operation', models.CharField(max_length=100)),
                ('description_operation', models.CharField(max_length=100)),
                ('montant_operation', models.DecimalField(decimal_places=2, max_digits=12)),
                ('date_operation', models.DateField(auto_now=True)),
                ('id_centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionParrainage.centre_orphelinat')),
            ],
        ),
    ]
