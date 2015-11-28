from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.AllDinosaursView.as_view() , name='all_dinosaurs'),
    url(r'^(?P<id>\d+)/$', views.GetDinosaurView.as_view() , name='get_dinosaur'),
    url(r'^new/$', views.NewDinosaurView.as_view() , name='new_dinosaur'),
]