# Generated by Django 5.1.2 on 2024-11-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_user', models.CharField(max_length=65)),
                ('login_user', models.CharField(max_length=45)),
                ('password_user', models.CharField(max_length=60)),
                ('confirmationpassword_user', models.CharField(max_length=60)),
                ('email_user', models.EmailField(max_length=254)),
                ('role_user', models.CharField(max_length=45)),
                ('dateincription_user', models.DateField(auto_now=True)),
            ],
        ),
    ]