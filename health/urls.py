from django.urls import path
from . import views
<<<<<<< HEAD
#from .utilis import update_symptoms
=======
>>>>>>> 63d7ce49692552376ba2a45a2431c65e7e06e6ed
urlpatterns = [
    path('chat-bot', views.chat_bot, name='chat_bot'),
    path('predict', views.predict, name='predict'),
    path('home',views.home,name='home'),
<<<<<<< HEAD
=======
    path('form-view',views.form_view),
>>>>>>> 63d7ce49692552376ba2a45a2431c65e7e06e6ed
    #path('save-symp',update_symptoms,name='symptoms-update'),
]

