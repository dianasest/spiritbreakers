# Generated by Django 3.2.8 on 2022-02-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20220209_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='balance',
            field=models.IntegerField(default=10000),
        ),
    ]