from django.test import TestCase
from lists.models import Item


class HomePageTest(TestCase):
    """Тест домашней страницы"""

    def test_used_index_template(self):
        """Используется index шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')



class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'Первый объект'
        first_item.save()

        second_item = Item()
        second_item.text = 'Второй объект'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Первый объект')
        self.assertEqual(second_saved_item.text, 'Второй объект')


class ListViewTest(TestCase):
    """Тест представления списка"""

    def test_uses_list_template(self):
        """тест: правильный шаблон списка"""
        response = self.client.get('/lists/unique-of-a-kind-list/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        """тест: отображаются все элементы списка"""

        Item.objects.create(text='items 1')
        Item.objects.create(text='items 2')

        response = self.client.get('/lists/unique-of-a-kind-list/')

        self.assertContains(response, 'items 1')
        self.assertContains(response, 'items 2')


class NewListTest(TestCase):
    """
    Тест нового списка
    """
    def test_can_save_a_POST_request(self):
        """тест: сохранение post-request"""

        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        """тест: переадресация после post-запроса"""
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertRedirects(response, '/lists/unique-of-a-kind-list/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/unique-of-a-kind-list/')


