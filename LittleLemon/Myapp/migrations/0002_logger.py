# Generated by Django 4.1.5 on 2023-07-21 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('time', models.TimeField()),
                ('table', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=10)),
                ('date', models.DateField()),
            ],
        ),
    ]
