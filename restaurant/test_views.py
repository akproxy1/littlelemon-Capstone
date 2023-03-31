from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.urls import reverse


class MenuViewTest(TestCase):
    menu_items = [
        MenuItem(title="chips", price=10, inventory=8),
        MenuItem(title="cream", price=50, inventory=82),
        MenuItem(title="mango", price=15, inventory=18),
        MenuItem(title="shrimp", price=100, inventory=38),
    ]

    def setup(self):
        MenuItem.objects.create(title="chips", price=10, inventory=8)
        MenuItem.objects.create(title="cream", price=50, inventory=82)
        MenuItem.objects.create(title="mango", price=15, inventory=18)
        MenuItem.objects.create(title="shrimp", price=100, inventory=38)

    def test_getall(self):
        self.setup()
        User.objects.create_user("user", "user@test.com", "testuser")
        user = User.objects.get(username="user")
        user_token, _ = Token.objects.get_or_create(user=user)
        api_client = APIClient()
        api_client.credentials(HTTP_AUTHORIZATION="Token " + user_token.key)
        url = reverse("restaurant:all_items")
        response = api_client.get(url)
        assert response.status_code == 200
        assert response.data == MenuSerializer(self.menu_items, many=True).data
        # return token
