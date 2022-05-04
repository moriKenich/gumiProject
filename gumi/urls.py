# -*- coding: utf-8 -*-
from django.urls import path
from .import views

app_name='gumi'

urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('search/',views.GumiListView.as_view(),name='search'),
    path('follow/<int:pk>/', views.follow, name='follow'),
    path('unfollow/<int:pk>/', views.follow, name='unfollow'),
    path('gumi_detail/<int:pk>/',views.DetailView.as_view(),name='gumi_detail'),
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('gumi/<int:category>',views.CategoryView.as_view(),name='gumi_cat'),
    path('gumi/<int:maker>',views.MakerView.as_view(),name='gumi_maker'),
    path('gumi/<int:hard>',views.HardView.as_view(),name='gumi_hard'),
    path('gumi/<int:powder>',views.PowderView.as_view(),name='gumi_powder'),
    ]
