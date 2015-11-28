from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Pizza, Brand, Ingredient

class GetPizzaView (View):
	def get (self, request, id):
		template = 'pizzas/pizza.html'
		pizza = get_object_or_404(Pizza, pk=id)
		context = {
			'pizza': pizza,
		}
		return render(request, template, context)

class AllPizzasView (View):
	def get (self, request):
		template = 'pizzas/pizzas.html'
		pizzas = Pizza.objects.all()
		context = {
			'pizzas': pizzas,
		}
		return render(request, template, context)

class NewPizzaView (View):
	def get (self, request):
		template = 'pizzas/new_pizza.html'
		return render(request, template)

	def post (self, request):
		name = request.POST.get('name', '')
		slices = request.POST.get('slices', '')
		id_brand = request.POST.get('brand', '')
		id_ingredient = request.POST.get('ingredient', '')
		brand = Brand.objects.get(pk=id_brand)
		ingredient = Ingredient.objects.get(pk=id_ingredient)


		pizza = Pizza(
			name=name,
			slices=slices,
			brand=brand,
		)

		pizza.save()
		pizza.ingredients.add(ingredient)

		return redirect('/pizzas')