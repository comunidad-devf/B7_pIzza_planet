from django.db import models
from django.utils import timezone

class Brand (models.Model):
	name = models.CharField(max_length=50, null=False)

	def __unicode__(self):
		return self.name

class Pizza (models.Model):
	name = models.CharField(max_length=50, null=False)
	slices = models.IntegerField(null=False)
	brand = models.ForeignKey('Brand', null=False)
	ingredients = models.ManyToManyField('Ingredient')

	def __unicode__(self):
		return self.name

class Ingredient (models.Model):
	ingredient = models.CharField(max_length=50, null=False)

	def __unicode__(self):
		return self.ingredient

class Ticket (models.Model):
	dinosaur = models.ForeignKey('dinosaurs.Dinosaur')
	pizza = models.ForeignKey('Pizza')
	date = models.DateTimeField(auto_now=False, default=timezone.now, null=False)

	def __unicode__(self):
		return self.dinosaur.name + " - " + str(self.date)