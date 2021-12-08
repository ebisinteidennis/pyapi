# Generated by Django 3.2.6 on 2021-12-08 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='completed',
            new_name='product_create',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='product_list',
        ),
        migrations.AddField(
            model_name='product',
            name='product_delete',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]