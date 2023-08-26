from django.urls import path
from .views import views

urlpatterns = [
    # 他のルート
    path('register/', views.register, name='register'),
    path('signin/', views.SignInView.as_view(), name='signin'),

]
