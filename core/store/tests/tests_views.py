from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

#
# @skip("demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_exmaple(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='Denny')
        Category.objects.create(name='Fleisch', slug='fleisch')
        Product.objects.create(category_id=1, title='Mett', created_by_id=1,
                               slug='mett', price='22.00', image='220px-2018-07-28-Mettbrötchen-9864.jpg')
    #
    # def test_url_allowed_hosts(self):
    #     """
    #     Test allowed hosts
    #     """
    #     response = self.c.get('/', HTTP_HOST='noaddress.com')
    #     self.assertEqual(response.status_code, 400)
    #     response = self.c.get('/', HTTP_HOST='yourdomain.com')
    #     self.assertEqual(response.status_code, 200)

    # def test_homepage_url(self):
    #     """
    #     Test homepage response status
    #     """
    #     response = self.c.get('/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_product_list_url(self):
    #     """
    #     Test category response status
    #     """
    #     response = self.c.get(
    #         reverse('store:category_list', args=['mett']))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_product_detail_url(self):
    #     """
    #     Test items response status
    #     """
    #     response = self.c.get(
    #         reverse('store:product_detail', args=['mett']))
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_homepage_html(self):
    #     """
    #     Example: code validation, search HTML for text
    #     """
    #     request = HttpRequest()
    #     engine = import_module(settings.SESSION_ENGINE)
    #     request.session = engine.SessionStore()
    #     response = product_all(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<title>Supermarket SHERIF</title>', html)
    #     self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
    #     self.assertEqual(response.status_code, 200)