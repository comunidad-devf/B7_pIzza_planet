from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^(?P<id>\d+)/$', views.GetPizzaView.as_view() , name='get_pizza'),
    url(r'^$', views.AllPizzasView.as_view() , name='all_pizzas'),
    url(r'^new/$', views.NewPizzaView.as_view() , name='new_pizza'),
]