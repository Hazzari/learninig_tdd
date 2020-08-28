#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Функциональный тест действий пользователя на сайте
'''

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    '''Тест нового посетителя'''

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()


    def test_can_start_a_list_and_retrievee_it_later(self):
        '''Создать список и получить его позже'''

        # Открывая браузер и заходим на наш сайт:
        self.browser.get('http://127.0.0.1:8000')

        # проверяем правильная ли у нас страница:
        # >>> Заголовок и шапка страницы указывают что это список дел
        self.assertIn('To-Do', self.browser.title)


        # Пользователю предлагается ввести элемент списка
        # Пользователь набирает в текстовом поле "Сходить в магазин за продуктами"
        # Пользователь нажимает enter, страница обновляется, и теперь страница содержит:
        # "1: Сходить в магазин за продуктами" в качестве элемента списка
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