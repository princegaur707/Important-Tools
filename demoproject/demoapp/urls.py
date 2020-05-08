from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('add/<int:a>/<int:b>',views.add,name='add'),
   path('multiply/<int:a>/<int:b>',views.multiply,name='multiply'),
   path('divide/<int:a>/<int:b>',views.divide,name='divide'),
   path('calculate/<str:eq>',views.calculate,name='eq')
]