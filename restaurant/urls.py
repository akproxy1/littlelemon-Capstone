from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

app_name = "restaurant"
urlpatterns = [
    path("", views.index, name="index"),
    path("api-token-auth/", obtain_auth_token),
    path("menu-items/", views.MenuItemView.as_view(), name="all_items"),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
]
