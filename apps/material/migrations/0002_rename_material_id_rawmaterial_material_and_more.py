# Generated by Django 5.0.3 on 2024-03-09 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rawmaterial',
            old_name='material_id',
            new_name='material',
        ),
        migrations.RenameField(
            model_name='rawmaterial',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='warehouse',
            old_name='material_id',
            new_name='material',
        ),
    ]
