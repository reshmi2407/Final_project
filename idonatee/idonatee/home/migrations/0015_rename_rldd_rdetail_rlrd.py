# Generated by Django 4.0.6 on 2023-03-16 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_signupp_confirmpassword'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rdetail',
            old_name='rldd',
            new_name='rlrd',
        ),
    ]
