# Generated by Django 3.1.4 on 2021-04-04 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('girlfriend', models.CharField(max_length=64)),
                ('boyfriend', models.CharField(max_length=64)),
            ],
        ),
    ]
