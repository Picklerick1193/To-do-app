"""
URL configuration for todolist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base import views 
from django.contrib.auth.decorators import login_required
from base.views import  todo_you
from base.views import completed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('signup/', views.sign_up, name='signup'),
    path('logout/', views.logout_user, name='logout'),
    path('todopage',todo_you,name='todopage'),
    path('edit_todo/<int:id>',views.edit_todo,name='edit_todo'),
    path('completed/<int:id>',views.completed,name='completed'),
    path('deleted/<int:id>',views.deleted, name='deleted'),
    path('tambola/',views.tambola,name='tambola'),
    path('generate_number/',views.generate_number, name='generate_number')
]