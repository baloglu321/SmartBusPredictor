from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/home

urlpatterns = [



path("", views.home, name="home"),
path("home", views.home),
path("eyüpsultan", views.eyüpsultan,name="Eyüpsultan"),
path("pendik", views.pendik,name="Pendik"),
path("emirgan", views.emirgan,name="Emirgan"),
path("taksim", views.taksim,name="Taksim"),
path("kadıköy", views.kadıköy,name="Kadıköy"),
path("karaköy", views.karaköy,name="Karaköy"),
path("beşiktaş", views.beşiktaş,name="Beşiktaş"),
path("ortaköy", views.ortaköy,name="Ortaköy"),
path("üsküdar", views.üsküdar,name="Üsküdar"),
path("kuzguncuk", views.kuzguncuk,name="Kuzguncuk"),

]
