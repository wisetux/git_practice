# Generated by Django 3.2.3 on 2021-05-19 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone', models.IntegerField()),
                ('standard', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
            ],
        ),
    ]