# Generated by Django 3.1.2 on 2021-08-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_complain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complain',
            field=models.CharField(max_length=9000),
        ),
        migrations.AlterField(
            model_name='complain',
            name='word',
            field=models.CharField(max_length=19),
        ),
    ]
