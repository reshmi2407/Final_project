# Generated by Django 4.0.6 on 2023-05-25 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_odonreq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orecreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('Org_req_to_rec', models.CharField(max_length=20)),
            ],
        ),
    ]
