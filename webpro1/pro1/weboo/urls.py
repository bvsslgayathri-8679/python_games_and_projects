from django.urls import path

from . import views

urlpatterns= [
    path('',views.index,name='index'),
    path('index.html',views.index,name='index'),
    path('contact.html',views.contact,name='contact'),
    path('intro.html',views.intro,name='intro'),
    path('lists.html',views.lists,name='lists'),
    path('tables.html',views.tables,name='tables'),
    path('fontsandimages.html',views.fontsandimages,name='fontsandimages')
]