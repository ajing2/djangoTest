# Generated by Django 2.0.3 on 2018-07-26 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=50)),
                ('telphone', models.CharField(max_length=30)),
            ],
        ),
    ]
