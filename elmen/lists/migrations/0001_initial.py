# Generated by Django 3.0.6 on 2020-08-29 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=300)),
                ('long_description', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.List')),
                ('web_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lists.Link')),
            ],
        ),
    ]
