# Generated by Django 4.1.3 on 2022-11-29 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(max_length=100, primary_key=True, serialize=False, verbose_name=int)),
                ('title', models.TextField(verbose_name=30)),
                ('image_url', models.TextField()),
                ('address', models.TextField(verbose_name=50)),
                ('detail_address', models.TextField(verbose_name=30)),
            ],
            options={
                'db_table': 'multiplex',
            },
        ),
    ]
