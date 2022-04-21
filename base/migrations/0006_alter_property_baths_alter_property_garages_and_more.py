# Generated by Django 4.0.3 on 2022-04-20 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_property_amenity1_alter_property_amenity2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='baths',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='garages',
            field=models.IntegerField(default='0', null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='property',
            name='rooms',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
