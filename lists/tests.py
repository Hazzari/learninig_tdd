from django.test import TestCase
from lists.models import Item


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


class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'Первый объект'
        first_item.save()

        second_item = Item()
        second_item.text = 'Второй объект'
        second_item.save()

        save_items = Item.objects.all()
        self.assertEqual(save_items.count(), 2)

        first_saved_item = save_items[0]
        second_saved_item = save_items[1]
        self.assertEqual(first_saved_item.text, 'Певый объект')
        self.assertEqual(second_saved_item.text, 'Втоой объект')
