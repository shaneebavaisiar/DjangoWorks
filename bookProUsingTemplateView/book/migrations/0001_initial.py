# Generated by Django 3.1.7 on 2021-04-27 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price', models.IntegerField()),
                ('author', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
            ],
        ),
    ]
