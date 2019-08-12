# Generated by Django 2.2.1 on 2019-08-09 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'City',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'State',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.City')),
            ],
            options={
                'verbose_name_plural': 'Locality',
                'ordering': ('name',),
                'unique_together': {('name', 'city')},
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='address.State'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=40, unique=True)),
                ('building_number', models.CharField(max_length=10)),
                ('postal_code', models.CharField(max_length=10)),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='address.Locality')),
            ],
            options={
                'verbose_name_plural': 'Address',
                'ordering': ('company_name',),
            },
        ),
    ]
