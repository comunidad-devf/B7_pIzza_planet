# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingredient', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pizza',
            name='ingredients',
            field=models.ManyToManyField(to='pizzas.Ingredient'),
        ),
    ]
