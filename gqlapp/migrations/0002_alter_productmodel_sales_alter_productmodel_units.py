# Generated by Django 5.1.4 on 2024-12-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gqlapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='Sales',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='Units',
            field=models.IntegerField(),
        ),
    ]