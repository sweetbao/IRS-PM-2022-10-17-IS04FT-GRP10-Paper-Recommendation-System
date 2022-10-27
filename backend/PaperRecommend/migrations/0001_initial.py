# Generated by Django 4.1.2 on 2022-10-27 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('retrievetime', models.DateTimeField(auto_now_add=True)),
                ('abstract', models.TextField()),
                ('publishTime', models.DateTimeField()),
                ('area', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('keywords', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Paper',
            },
        ),
    ]
