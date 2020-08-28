from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):
    '''Тест домашней страницы'''

    def test_root_urls_resolves_to_home_page_view(self):
        '''тест: / url преобразуется в view домашней страницы'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
