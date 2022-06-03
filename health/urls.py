from django.urls import path
from . import views

urlpatterns = [
    path('chat-bot', views.chat_bot, name='chat_bot'),
    path('predict', views.predict, name='predict'),
    path('home',views.home,name='home')
    #path('save-symp',update_symptoms,name='symptoms-update'),
]
