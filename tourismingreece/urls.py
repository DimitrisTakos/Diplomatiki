from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about-us.html', views.about_us, name='about_us'),
]
