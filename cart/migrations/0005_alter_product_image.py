# Generated by Django 4.0.3 on 2022-04-25 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_rename_descritption_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_image'),
        ),
    ]
