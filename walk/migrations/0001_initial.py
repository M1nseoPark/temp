# Generated by Django 3.2.8 on 2021-10-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'park2',
                'managed': False,
            },
        ),
    ]
