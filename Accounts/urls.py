from django.urls import path
from . import views
urlpatterns = [
    
    path('login-register',views.FormRender,name="login-register"),
    path('register',views.registerPage,name="register"),
    path('login',views.loginpage,name="login"),
    path('logout',views.user_logout,name="logout")

]