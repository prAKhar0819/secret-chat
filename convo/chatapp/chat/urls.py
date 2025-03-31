from django.urls import path
import chat.views as views

urlpatterns = [
    path('', views.home, name='home'),  # Use views.home
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/', views.chat_view, name='chat_view'),  # Reference the chat_view function from views.py
]

