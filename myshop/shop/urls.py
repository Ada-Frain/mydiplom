from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('about/', views.about, name='about'),
    path('delivery/', views.delivery, name='delivery'),
    path('contacts/', views.contacts, name='contacts'),
    path('discounts/', views.discounts, name='discounts'),
    path('fandoms/', views.fandom_list, name='fandom_list'),
    re_path(r'^fandoms/(?P<fandom_slug>[-\w]+)/$', views.fandom_list, name='product_list_by_fandom'),
    re_path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    re_path(r'^$', views.product_list, name='search'),
    re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]