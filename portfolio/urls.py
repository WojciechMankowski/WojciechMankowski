from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('/<str:languages>', views.filter),
    path('delet', views.delet),
    path("update/<str:name>", views.update)
]