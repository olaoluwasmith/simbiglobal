# Generated by Django 4.1.7 on 2023-02-14 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=50)),
                ('category', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agriculture.category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agriculture.category')),
                ('subcategory', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agriculture.subcategory')),
            ],
            options={
                'verbose_name': 'Revenue',
                'verbose_name_plural': 'Revenue',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agriculture.category')),
                ('subcategory', models.ForeignKey(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='agriculture.subcategory')),
            ],
            options={
                'verbose_name': 'Expenses',
                'verbose_name_plural': 'Expenses',
                'ordering': ['-date'],
            },
        ),
    ]
