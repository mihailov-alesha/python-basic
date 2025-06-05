import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

class SearchTest(unittest.TestCase):
    """ Тестовый сценарий """

    def setUp(self):
        """Перед выполнением теста. Предварительная настройка браузера и переменных."""
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("prefs", {'intl.accept_languages': 'en'})
        
        # Для отладки используем headless режим
        options.add_argument('--headless=new')
        
        service = Service('chromedriver.exe')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.set_window_size(1920, 1080)

    def test_search_selenide(self):
        """Тест #1 - Открытие страницы и проверка заголовка"""
        try:
            # Шаг 1. Открытие страницы
            self.driver.get('https://search.yahoo.com/')
            self.assertIn('Yahoo Search', self.driver.title, 'Заголовок страницы не совпадает')

            # Шаг 2. Поиск "selenide"
            search_box = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.NAME, 'p'))
            )
            search_box.send_keys('selenide' + Keys.ENTER)
            
            # Шаг 3. Проверка первого результата
            # Универсальный селектор для результатов
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#web'))
            )
            
            # Получаем все результаты и берем первый
            results = self.driver.find_elements(By.CSS_SELECTOR, 'div.algo h3 a, div#web h3 a')
            self.assertTrue(len(results) > 0, "Не найдены результаты поиска")
            
            first_result = results[0]
            first_result_url = first_result.get_attribute('href')
            print(f"URL первого результата: {first_result_url}")
            self.assertIn('selenide.org', first_result_url, 'Первый результат не содержит selenide.org')
            first_result_text = first_result.text
            
            # Шаг 4. Переход в раздел изображений
            images_tab = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="images"]'))
            )
            images_tab.click()
            
            # Шаг 5. Проверка первого изображения
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'li.ld'))
            )
            
            images = self.driver.find_elements(By.CSS_SELECTOR, 'li.ld')
            self.assertTrue(len(images) > 0, "Не найдены изображения")
            
            first_image_desc = images[0].find_element(By.CSS_SELECTOR, 'span')
            image_text = first_image_desc.text.lower()
            print(f"Текст первого изображения: {image_text}")
            self.assertIn('selenide', image_text, 'Первое изображение не связано с selenide')
            
            # Шаг 6. Возврат в раздел "Все"
            all_tab = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href*="search"]'))
            )
            all_tab.click()
            
            # Шаг 7. Проверка первого результата после возврата
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#web'))
            )
            
            new_results = self.driver.find_elements(By.CSS_SELECTOR, 'div.algo h3 a, div#web h3 a')
            self.assertTrue(len(new_results) > 0, "Не найдены результаты после возврата")
            
            new_first_result_text = new_results[0].text
            print(f"Текст первого результата после возврата: {new_first_result_text}")
            self.assertEqual(first_result_text, new_first_result_text, 'Первый результат изменился после возврата')
            
        except Exception as e:
            # Сохраняем скриншот при ошибке
            self.driver.save_screenshot("error_screenshot.png")
            raise e

    def tearDown(self):
        """После выполнения теста. Закрытие браузера"""
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
