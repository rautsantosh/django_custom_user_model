from servers import views
from django.urls import path

urlpatterns = [
    path('add_server/', views.add_server, name='add_server'),
]

