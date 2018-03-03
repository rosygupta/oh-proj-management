from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from project_admin.views import HomeView, LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(HomeView.as_view(), login_url='login/'), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]
