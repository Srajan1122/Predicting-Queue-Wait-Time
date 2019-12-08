from . import views
from django.urls import re_path 


urlpatterns = [
    re_path(r'^Documentation/',views.Documentation,name='Documentation'),
    re_path(r'^Single/',views.Single,name='Single'),
    re_path(r'^Complete/',views.Complete,name='Complete'),
    re_path(r'^Future/',views.Future,name='Future'),
    
]

