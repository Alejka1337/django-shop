# Generated by Django 4.1.1 on 2022-10-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ecomm', '0005_productimages_title_alter_productimages_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(db_index=True, verbose_name='comment')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='name')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ecomm.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
    ]
