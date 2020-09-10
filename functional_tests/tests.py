#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Функциональный тест действий пользователя на сайте."""
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase

MAX_WAIT = 3


class NewVisitorTest(LiveServerTestCase):
    """Тест нового посетителя"""

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def wait_for_row_in_lists_table(self, row_text):
        """подтверждение строки в таблице списка"""
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """Создать список и получить его позже"""

        # Открывая браузер и заходим на наш сайт:
        self.browser.get(self.live_server_url)

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

        self.wait_for_row_in_lists_table('1: Сходить в магазин за продуктами')

        # Текстовое поле по прежнему приглашает пользователя добавить еще один элемент.
        # Пользователь вводит "Купить молоко и хлеб" и нажимает enter
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Купить молоко и хлеб')
        input_box.send_keys(Keys.ENTER)

        # Страница обновляется, и теперь показывает оба элемента списка
        self.wait_for_row_in_lists_table('1: Сходить в магазин за продуктами')
        self.wait_for_row_in_lists_table('2: Купить молоко и хлеб')

        # Пользователь думает, запомнит ли сайт его список и видит что сайт сгенерировал для него уникальный URL-адрес
        # об этом выводится небольшой текст с обяснениями.
        # Пользователь посещает этот URL и видит что он отображает правильно его список.
        # Пользователь заканчивает работу с сайтом
        # ------- >>>>> Конец сценария

        self.fail('Написать следующий тест')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        """тест: многочисленные пользователи могут создавать списки по разным url"""
        # Первый пользователь создает новый список
        self.browser.get(self.live_server_url)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Сходить в магазин за продуктами')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_lists_table('1: Сходить в магазин за продуктами')

        # пользователь видит что его список имеет уникальный url
        first_user_list_url = self.browser.current_url
        self.assertRegex(first_user_list_url, '/lists/.+')

        # Теперь приходит новый пользователь на сайт.

        # ##  Мы используем новый сеанс браузера для обеспечения изолированности от первого пользователя. cookie и др.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Второй пользователь посещяет домашнюю страницу.Нет никаких признаков списка первого пользователя
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Сходить в магазин за продуктами', page_text)
        self.assertNotIn('Купить молоко и хлеб', page_text)

        # Второй пользователь начинает новый список, вводя новый элемент.

        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Купить молоко')
        input_box.send_keys(Keys.ENTER)
        self.wait_for_row_in_lists_table('1: Купить молоко')

        # второй пользователь получает уникальный URL адрес
        second_user_list_url = self.browser.current_url
        self.assertRegex(second_user_list_url, 'lists/.+')
        self.assertNotEqual(second_user_list_url, first_user_list_url)

        # Нет никаокго следа от списка первого пользователя
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('ходить в магазин за продуктами', page_text)
        self.assertIn('Купить молоко', page_text)

        self.fail('Написать следующий тест')
