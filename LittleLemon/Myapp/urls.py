
from django.urls import path
from Myapp import views



urlpatterns = [
    path('',views.home),
    path('about/',views.about,name='about'),
    path('menu/',views.menu,name='menu'),
    path('menu_item/<int:pk>',views.display_menu_items,name='menu_item'),
    path('reservation/',views.reservation,name='reservation'),
    path('submission/',views.submission,name='submission'),
    ]