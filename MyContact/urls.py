from django.urls import path
from . import views

urlpatterns = [
    # path('', views.controleform1, name='contact'),  # URL pour accéder au formulaire
    path('', views.controleform2, name='contact')
]
