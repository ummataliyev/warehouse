# Generated by Django 5.0.3 on 2024-03-09 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'material',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.material')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.product')),
            ],
            options={
                'db_table': 'raw_material',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remainder', models.FloatField()),
                ('price', models.FloatField()),
                ('material_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.material')),
            ],
        ),
    ]
