# Generated by Django 4.1.7 on 2023-03-06 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_commande_quartier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
