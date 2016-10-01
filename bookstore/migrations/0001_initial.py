# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('publication_version', models.CharField(max_length=10)),
                ('authors', models.ManyToManyField(to='bookstore.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(to='bookstore.Publisher'),
        ),
    ]
