from django.test import TestCase
from django.urls import reverse
from .models import Product

class ProductsViewsTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name='Test Product', price=50, description='Test Description')

    def test_products_view(self):
        url = reverse('products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_detail_product_view(self):
        url = reverse('detail_product', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_create_product_view(self):
        url = reverse('create_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Create Product')

    def test_create_view(self):
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        response = self.client.post(url, {'name': 'New Product', 'price': 100, 'description': 'New Description'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 2)

    def test_my_products_view(self):
        url = reverse('my_products', args=[self.product.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_delete_product_view(self):
        url = reverse('delete_product', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Product.objects.count(), 0)

    def test_update_view(self):
        url = reverse('update', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)
        response = self.client.post(url, {'name': 'Updated Product', 'price': 75, 'description': 'Updated Description'})
        self.assertEqual(response.status_code, 302)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'Updated Product')
        self.assertEqual(self.product.price, 75)
        self.assertEqual(self.product.description, 'Updated Description')
