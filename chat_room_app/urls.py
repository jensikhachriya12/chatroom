"""
URL configuration for chat_room project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('demo',demo,name='demo'),
     path('login/',admin_login, name="admin_login"),
     path('logins/',logins,name='logins'),
     path('dashboard/',dashboard,name="dashboard"),
     path('logout/', admin_logout,name="logout"),
     path('customer/',customer,name="customer"),
     path('add-customer/',add_customer,name="add_customer"),
     path('get-customer/<int:id>',get_customer,name="get_customer"),
     path('edit-customer/',edit_customer,name="edit_customer"),
     path('delete-customer/<int:id>',delete_customer,name="delete_customer"),
     path('chatroom/',chatroom,name="chatroom"),
     path('add-chatroom/',add_chatroom,name="add_chatroom"),
     path('get-chatroom/<int:id>',get_chatroom,name="get_chatroom"),
     path('edit-chatroom/',edit_chatroom,name="edit_chatroom"),
     path('delete-chatroom/<int:id>',delete_chatroom,name="delete_chatroom"),
     path('view/',view,name="view"),
     path('chat-view/<int:id>',chat_view,name="chat_view"),
     path('edit-profile/',edit_profile,name="edit_profile"),
     path('chatroom-view/<int:id>',chatroom_view,name="chatroom_view"),
    path('edit_customer-profile/',edit_customer_profile,name="edit_customer_profile"),
    path('add-new-chat/',add_new_chat,name="add_new_chat"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
