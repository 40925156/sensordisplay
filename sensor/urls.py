from django.conf.urls import url
from sensor import views
urlpatterns = [
    url(r'^$', views.Temperature,name='sensor.temperature'),
    url(r'^temperature_api', views.temperature_api.as_view(),name='sensor.temperature_api'),
    url(r'^get_temperature', views.Temperature,name='sensor.get_Temperature'),
]
