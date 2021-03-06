# Generated by Django 3.2.9 on 2021-11-19 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('industria', models.CharField(max_length=200)),
                ('trabajo', models.CharField(max_length=200)),
                ('empresa', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
