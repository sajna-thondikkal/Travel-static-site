# Generated by Django 4.1.2 on 2022-10-14 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sajnatravelapp', '0002_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dest',
            name='price',
            field=models.IntegerField(),
        ),
    ]