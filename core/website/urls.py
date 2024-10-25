from django.urls import path
from . import views

app_name='website'

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact') ,
    path('elements',views.elements,name='elements'),
    path('newsletter',views.newsletter,name='newsletter'),
]