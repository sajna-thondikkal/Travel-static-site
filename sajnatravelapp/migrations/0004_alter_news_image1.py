# Generated by Django 4.1.2 on 2022-10-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sajnatravelapp', '0003_alter_dest_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image1',
            field=models.ImageField(upload_to='picture1'),
        ),
    ]