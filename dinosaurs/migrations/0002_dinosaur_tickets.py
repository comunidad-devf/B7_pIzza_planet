# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0003_ticket'),
        ('dinosaurs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dinosaur',
            name='tickets',
            field=models.ManyToManyField(to='pizzas.Pizza', through='pizzas.Ticket'),
        ),
    ]
