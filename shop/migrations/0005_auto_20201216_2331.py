# Generated by Django 3.0 on 2020-12-16 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_auto_20201215_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('zipcode', models.CharField(max_length=255, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='amount',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='posted_date',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Customer'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Order'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.Customer'),
        ),
    ]
