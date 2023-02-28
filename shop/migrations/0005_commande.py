# Generated by Django 4.1.7 on 2023-02-22 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=300)),
                ('Nom', models.CharField(max_length=150)),
                ('Email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=200)),
                ('Ville', models.CharField(max_length=200)),
                ('Pays', models.CharField(max_length=300)),
                ('code_postal', models.CharField(max_length=300)),
                ('date_commande', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-date_commande'],
            },
        ),
    ]