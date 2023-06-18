# Generated by Django 4.2.2 on 2023-06-17 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('color', models.CharField(default='none', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.IntegerField(unique=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=100)),
                ('is_sold', models.BooleanField(default=False)),
                ('product_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_s3_location', models.CharField(max_length=500)),
                ('product_id', models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.productdetail')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.SET_DEFAULT, to='product.productcategory'),
        ),
    ]
