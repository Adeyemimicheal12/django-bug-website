from django.urls import path
from .views import register_page,logout_confirm, profile_confirm
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns=[
    path('register/', register_page, name="Create-account"),
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="user-login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="user-logout"),
    path('confirm/logout/', logout_confirm, name="logout-confirm"),
    path('profile/', profile_confirm, name="profile-name")
]