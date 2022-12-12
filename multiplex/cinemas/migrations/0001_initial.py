# Generated by Django 4.1.3 on 2022-11-29 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.TextField(verbose_name=120)),
                ('director', models.TextField(verbose_name=20)),
                ('description', models.TextField()),
                ('pster_url', models.TextField()),
                ('running_time', models.IntegerField()),
                ('age_ratin', models.IntegerField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]