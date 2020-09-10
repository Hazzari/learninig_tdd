from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_used_index_template(self):
        """Используется index шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/index.html')

    def test_can_save_a_POST_request(self):
        """тест: сохранение post-request"""
        response = self.client.post('/', data={'item_text': 'A new list item'})

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/index.html')
