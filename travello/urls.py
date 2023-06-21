from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.index, name = 'index'),    
    path("destinations/", views.destination_list), # To View the Api(GET), add record(POST)
    path("destinations/<int:id>", views.destination_detail) # To get(GET) single record by id, update(PUT), delete(DELETE)

]

urlpatterns = format_suffix_patterns(urlpatterns)