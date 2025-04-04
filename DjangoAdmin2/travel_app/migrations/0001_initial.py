# Generated by Django 5.1.1 on 2024-12-28 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'counties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taiwan',
            fields=[
                ('taiwen_id', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=20)),
                ('town', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'taiwen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('travel_id', models.AutoField(primary_key=True, serialize=False)),
                ('travel_name', models.CharField(max_length=50)),
                ('travel_txt', models.TextField(blank=True, null=True)),
                ('tel', models.CharField(blank=True, max_length=50, null=True)),
                ('travel_address', models.TextField()),
                ('region', models.CharField(max_length=10)),
                ('town', models.CharField(max_length=10)),
                ('travel_linginfo', models.TextField(blank=True, null=True)),
                ('opentime', models.TextField(blank=True, null=True)),
                ('image1', models.TextField(blank=True, null=True)),
                ('image2', models.TextField(blank=True, null=True)),
                ('image3', models.TextField(blank=True, null=True)),
                ('px', models.DecimalField(blank=True, db_column='Px', decimal_places=8, max_digits=12, null=True)),
                ('py', models.DecimalField(blank=True, db_column='Py', decimal_places=8, max_digits=12, null=True)),
                ('website', models.TextField(blank=True, null=True)),
                ('ticketinfo', models.TextField(blank=True, null=True)),
                ('parkinginfo', models.TextField(blank=True, null=True)),
                ('upload', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'travel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TravelClass',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'travel_class',
                'managed': False,
            },
        ),
    ]
