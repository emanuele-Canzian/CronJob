
from django.contrib import admin
from django.urls import path
from Cronjob_Dev import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name="register"),
    path('register/', views.register_user, name="register"),
    path('crone/', views.crone, name="crone")
]
