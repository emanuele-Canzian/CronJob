# Generated by Django 2.2.6 on 2019-10-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CronJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
                ('url', models.URLField(default='', max_length=255)),
                ('authentification', models.BooleanField(default=False)),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('minute', models.CharField(default='', max_length=30)),
                ('hour', models.CharField(default='', max_length=30)),
                ('dayOfMonth', models.CharField(default='', max_length=30)),
                ('month', models.CharField(default='', max_length=30)),
                ('weekday', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
