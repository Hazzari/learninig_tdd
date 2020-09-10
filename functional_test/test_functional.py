#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Функциональный тест действий пользователя на сайте."""
import time

from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    """Тест нового посетителя"""

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Создать список и получить его позже"""

        # Открывая браузер и заходим на наш сайт:
        self.browser.get('http://127.0.0.1:8000')

        # проверяем правильная ли у нас страница:
        # >>> Заголовок и шапка страницы указывают что это список дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Пользователю предлагается ввести элемент списка
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Введите задачу')

        # Пользователь набирает в текстовом поле "Сходить в магазин за продуктами"
        input_box.send_keys('Сходить в магазин за продуктами')
        # Пользователь нажимает enter, страница обновляется, и теперь страница содержит:
        # "1: Сходить в магазин за продуктами" в качестве элемента списка
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == "1: Сходить в магазин за продуктами" for row in rows),
                        'Новый элемент списка не появился в таблице')

        # Текстовое поле по прежнему приглашает пользователя добавить еще один элемент.
        # Пользователь вводит "Купить молоко и хлеб" и нажимает enter
        # Страница обновляется, и теперь показывает оба элемента списка
        # Пользователь думает, запомнит ли сайт его список и видит что сайт сгенерировал для него уникальный URL-адрес
        # об этом выводится небольшой текст с обяснениями.
        # Пользователь посещает этот URL и видит что он отображает правильно его список.
        # Пользователь заканчивает работу с сайтом
        # ------- >>>>> Конец сценария

        self.fail('Написать следующий тест')


if __name__ == '__main__':
    unittest.main()
