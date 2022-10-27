# Generated by Django 4.1.1 on 2022-10-26 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.TextField(db_index=True, verbose_name='comment'),
        ),
    ]