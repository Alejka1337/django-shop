# Generated by Django 4.1 on 2022-09-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0002_сharacteristics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='сharacteristics',
            old_name='pol',
            new_name='Sex',
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/%Y', verbose_name='Фото'),
        ),
    ]
