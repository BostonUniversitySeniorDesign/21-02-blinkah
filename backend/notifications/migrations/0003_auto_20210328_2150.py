# Generated by Django 3.1.6 on 2021-03-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20210328_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeunit',
            name='last_seen',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
