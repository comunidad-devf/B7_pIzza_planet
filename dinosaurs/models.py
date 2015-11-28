from django.db import models

class Dinosaur (models.Model):
	name = models.CharField(max_length=50, null=False)
	age = models.IntegerField(null=False)
	color = models.CharField(max_length=50, null=False)
	dangerous = models.BooleanField(null=False)
	tickets = models.ManyToManyField('pizzas.Pizza', through='pizzas.Ticket')

	def __unicode__(self):
		return self.name + " " + str(self.age)