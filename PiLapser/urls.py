from django.conf.urls import url
from PiLapser import views

urlpatterns = [
	url(r'^piLapse/$', views.get_fields),
	url(r'^move_pos/$', views.move_pos),
	url(r'^move_neg/$', views.move_neg),
    url(r'^status/$', views.render_status),
]
