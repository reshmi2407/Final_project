# Generated by Django 4.0.6 on 2023-03-02 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_odetail_alter_detail_mobno_alter_rdetail_rmobno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('hfname', models.CharField(max_length=20)),
                ('hid', models.CharField(max_length=20)),
                ('hemail', models.EmailField(max_length=254)),
                ('hmobno', models.IntegerField()),
                ('haddress', models.CharField(max_length=30)),
                ('bbp', models.CharField(max_length=10)),
                ('obp', models.CharField(max_length=10)),
                ('himage', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]
