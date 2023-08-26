from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from shop.models import Product, Shop, Recipe
from user.models import User
from shop.views.purchase_view import purchase, purchase_after
from shop.views.recipe_view import recipe_all, recipe_detail
from django.core.files.uploadedfile import SimpleUploadedFile

class PurchaseViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        dummy_image = SimpleUploadedFile(name='test_image.jpg', content=b'file_content', content_type='image/jpeg')
        self.user = User.objects.create(email="test@example.com", name="Test User")
        self.shop = Shop.objects.create(name="Test Shop", owner=self.user)
        self.product = Product.objects.create(name="Test Product", shop=self.shop, img=dummy_image)

        # ビューへのURLを取得
        self.purchase_url = reverse('purchase')  # 'purchase'はurls.pyで定義したビューの名前です。
        self.purchase_after_url = reverse('purchase_after')  # 同上

    def test_purchase_view(self):
        request = self.factory.get(self.purchase_url)
        response = purchase(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.product.name.encode(), response.content)

    def test_purchase_after_view(self):
        request = self.factory.get(self.purchase_after_url)
        response = purchase_after(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.product.name.encode(), response.content)


class RecipeViewTest(TestCase):
    def setUp(self):
        self.client = Client()  # テストクライアントのインスタンスを作成
        self.user = User.objects.create(email="test@example.com", name="Test User")
        self.shop = Shop.objects.create(name="Test Shop", owner=self.user)
        self.recipe = Recipe.objects.create(title="Test Recipe", content="Test Content", created_by=self.user, shop=self.shop)
        self.recipe_all_url = reverse('recipe')
        self.recipe_detail_url = reverse('recipe_detail', args=[1])

    def test_recipe_all_view(self):
        response = self.client.get(self.recipe_all_url)  # テストクライアントを使用してGETリクエストを行います

        self.assertEqual(response.status_code, 200)
        # self.assertIn(self.recipe.title, response.content.decode())  # response.contentはbytes型なのでdecodeしてstr型に変換

    def test_recipe_detail_view(self):
        response = self.client.get(self.recipe_detail_url)  # テストクライアントを使用してGETリクエストを行います

        self.assertEqual(response.status_code, 200)
        # self.assertIn(self.recipe.title, response.content.decode())