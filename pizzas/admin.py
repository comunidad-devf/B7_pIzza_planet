from django.contrib import admin

from .models import Pizza, Brand, Ingredient, Ticket


admin.site.register(Pizza)
admin.site.register(Brand)
admin.site.register(Ingredient)
admin.site.register(Ticket)