# Generated by Django 4.0.6 on 2023-05-25 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_hdonreq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hdonreq',
            old_name='org_req_to_hos',
            new_name='hospital_req_to_don',
        ),
    ]
