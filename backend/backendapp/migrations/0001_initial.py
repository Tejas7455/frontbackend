# Generated by Django 5.0.5 on 2024-05-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=20)),
                ('esal', models.IntegerField()),
                ('addr', models.CharField(max_length=50)),
            ],
        ),
    ]