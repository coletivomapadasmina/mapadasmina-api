# Generated by Django 2.1 on 2018-08-11 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_create_causes'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenderIdentity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
    ]