
from django.contrib import admin
from django.urls import path
from Cronjob_Dev import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
]
