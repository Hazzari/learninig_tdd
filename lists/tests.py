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

    # def test_root_urls_resolves_to_home_page_view(self):
    #     """тест: / url преобразуется в view домашней страницы"""
    #     found = resolve('/')
    #     self.assertEqual(found.func, home_page)
    #
    # def test_home_page_returns_correct_html(self):
    #     """тест: Домашняя страница возвращает правильный html"""
    #
    #     response = self.client.get('/')
    #
    #     html = response.content.decode('utf-8')
    #
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.endswith('</html>'))


