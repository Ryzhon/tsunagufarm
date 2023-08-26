from django.test import TestCase
from ..models import Shop, Product, Recipe,  Tag
from user.models import User

class ShopModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User")  # nameの値を変更

    def test_shop_creation(self):
        shop = Shop.objects.create(name="Test Shop", owner=self.user)
        self.assertEqual(shop.name, "Test Shop")
        self.assertEqual(shop.owner, self.user)

class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User")  # nameの値を変更
        self.shop = Shop.objects.create(name="Test Shop", owner=self.user)

    def test_product_creation(self):
        product = Product.objects.create(name="Test Product", shop=self.shop)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.shop, self.shop)

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@example.com", name="Test User")  # nameの値を変更
        self.shop = Shop.objects.create(name="Test Shop", owner=self.user)
        self.tag = Tag.objects.create(name="Test Tag")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(title="Test Recipe", content="Test Content", created_by=self.user, shop=self.shop)
        recipe.tags.add(self.tag)
        self.assertEqual(recipe.title, "Test Recipe")
        self.assertIn(self.tag, recipe.tags.all())
