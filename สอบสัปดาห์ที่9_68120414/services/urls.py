from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),               # หน้าแรก
    path('products/', views.products, name='products'), # หน้าแคตตาล็อก
    path('feedback/', views.feedback, name='feedback'), # หน้าข้อเสนอแนะ
]