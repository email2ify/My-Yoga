from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('article/', views.yoga_email, name='yoga_email'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('article/<int:pk>/update/', views.update_comment,
         name='update_comment'),
    path('article/<pk>/deleteView/', views.delete_comment,
         name='DeleteView')
]
