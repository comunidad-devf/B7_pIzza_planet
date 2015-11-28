from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect

from .models import Dinosaur

class GetDinosaurView (View):
	def get (self, request, id):
		template = 'dinosaurs/dinosaur.html'
		dinosaur = get_object_or_404(Dinosaur, pk=id)
		#dinosaur = Dinosaur.objects.get(pk=id)
		context = {
			'dinosaur': dinosaur,
		}
		#return HttpResponse(dinosaur)
		return render(request, template, context)


class AllDinosaursView (View):
	def get (self, request):
		template = 'dinosaurs/dinosaurs.html'
		dinosaurs = Dinosaur.objects.all()
		context = {
			'dinosaurs': dinosaurs,
		}
		return render(request, template, context)

class NewDinosaurView (View):
	def get (self, request):
		template = 'dinosaurs/new_dinosaur.html'
		return render(request, template)

	def post (self, request):
		name = request.POST.get('name', '')
		age = request.POST.get('age', '')
		color = request.POST.get('color', '')
		dangerous = request.POST.get('dangerous', '')

		dinosaur = Dinosaur(
			name=name,
			age=age,
			color=color,
			dangerous=dangerous,
		)

		dinosaur.save()

		return redirect('/dinosaurs')