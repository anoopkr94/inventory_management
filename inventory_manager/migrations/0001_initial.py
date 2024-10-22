# Generated by Django 3.1.3 on 2021-03-18 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100, null=True)),
                ('size', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('mrp', models.FloatField()),
                ('stock', models.IntegerField(default=0)),
                ('reorder_level', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('mrp', models.FloatField()),
                ('qty', models.IntegerField(default=0)),
                ('total', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=100)),
                ('mrp', models.FloatField()),
                ('price', models.FloatField()),
                ('qty', models.IntegerField(default=0)),
                ('total', models.FloatField()),
                ('profit', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='cartitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory_manager.item')),
            ],
        ),
    ]
