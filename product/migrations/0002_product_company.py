# Generated by Django 4.2.2 on 2023-06-17 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
