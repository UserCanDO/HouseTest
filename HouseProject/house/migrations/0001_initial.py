# Generated by Django 4.2 on 2023-04-28 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.TextField()),
                ('street_name', models.TextField()),
                ('city', models.TextField()),
                ('postal_code', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HousePurchase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('home_type', models.TextField(choices=[('bungalow', 'bungalow'), ('duplex', 'duplex')])),
                ('date_of_purchase', models.DateField(auto_now_add=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
        ),
    ]
