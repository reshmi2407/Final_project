# Generated by Django 4.0.6 on 2023-05-21 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_recreq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recreq',
            old_name='Select_category_of_Receiving',
            new_name='scor',
        ),
    ]
