# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dinosaurs', '0001_initial'),
        ('pizzas', '0002_auto_20151127_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('dinosaur', models.ForeignKey(to='dinosaurs.Dinosaur')),
                ('pizza', models.ForeignKey(to='pizzas.Pizza')),
            ],
        ),
    ]
