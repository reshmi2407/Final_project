# Generated by Django 4.0.6 on 2023-05-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_rename_qan_quick_qaddress_remove_quick_qage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orgreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('scod', models.CharField(max_length=20)),
            ],
        ),
    ]
