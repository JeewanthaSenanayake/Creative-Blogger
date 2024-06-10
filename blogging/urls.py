from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.product_list, name='product_list'),
    path('<int:pk>/<int:id>/', views.product_detail, name='product_detail'),
    path('<int:pk>/blog/', views.product_detail_no_login, name='product_detail_no_login'),
    path('<int:pk>/<int:id>/blogs/', views.product_detail_login, name='product_detail_login'),
    path('<int:pk>/<int:id>/edit/', views.edit_product, name='edit_product'),
    path('<int:pk>/<int:id>/delete/', views.delete_product, name='delete_product'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('<int:id>/profile_pic/', views.upload_profile_pic, name='upload_profile_pic'),
    path('<int:id>/creat_blog/', views.create_blog, name='creat_blog'),
    path('<int:id>/dashboard/', views.dashboard, name='dashboard'),
    path('like_blog/', views.like_blog, name='like_blog'),
    path('comments/', views.comments, name='comments'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)