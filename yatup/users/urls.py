from django.contrib.auth.views import LogoutView
from django.urls import include, path
from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html')),
    path('signup/', views.SignUp.as_view(), name='signup')
]