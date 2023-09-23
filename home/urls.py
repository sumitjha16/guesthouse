from django.urls import path
from .  import views

urlpatterns = [
path('', views.index,name="index"),
path('htw/', views.htw,name="HTW"),
path('contact/', views.contact,name="contact"),
path('book/', views.book_view,name="book"),
path('room/', views.room,name="room"),
path('book_room/', views.book_room, name='book_room'),
path('payment/<int:total_amount>/', views.payment, name='payment')

]
