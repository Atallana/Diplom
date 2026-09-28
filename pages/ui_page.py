from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


# создание класса
class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    SELECTOR = ('[class="film-poster styles_root__J_gIg '
                'styles_rootInLight__iqWuw image styles_root__95qkI"]'
                )
    SEARCH = (By.XPATH, "//input[@placeholder='Фильмы, сериалы, персоны']")
    TOP_RESULT = (By.XPATH, "//section[@data-testid='search-top-result']//a[@data-test-id='next-link']//span[contains(@class, 'mainTitle')]")
    TICKET_BTN = (By.XPATH, "//nav[contains(@class, 'kinopoisk-header-featured-menu')]//a[contains(@href, '/movies-in-cinema/')]")
    ONLINE_BTN = (By.CSS_SELECTOR, 'a[data-tid="acc26a70"]')
    SHOP_BTN = (By.XPATH, "//a[@data-tid='de7c6530']")
    FILMS_BTN = (By.XPATH, "//a[contains(@class, 'styles_root')]//span[contains(@class, 'styles_title')]")

    @allure.step("Открыть главную страницу: {url}")
    def open_main_page(self, url="https://www.kinopoisk.ru/"):
        self.driver.get(url)
        self.close_ad_if_present()  # <-- закрываем рекламу, если она есть
        return self.driver

    @allure.step("Закрыть рекламное окно, если оно присутствует")
    def close_ad_if_present(self, timeout=5):
        """Закрывает модальное рекламное окно, если оно появилось.
        Если окна нет — просто продолжает выполнение"""
        try:
            close_btn = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button[data-tid="CloseButton"][aria-label="Закрыть коммуникацию"]')
                )
            )
            close_btn.click()

            # Ждём, пока модалка исчезнет из DOM
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.ReactModalPortal'))
            )
        except Exception:
            pass

    @allure.step("Ввести название фильма в поиск: {movie_name}")
    def main_search(self, movie_name):
        """Метод вводит название фильма"""
        search_input = self.wait.until(
            EC.element_to_be_clickable(self.SEARCH)
        )
        search_input.click()

        # Вводим точное название фильма
        search_input.send_keys(movie_name)
        search_input.send_keys(Keys.ENTER)

    @allure.step("Выбрать первый результат из блока 'Возможно, вы искали'")
    def search_top_result(self):
        """Поиск фильма по точному названию
        и выбор по первому результату в блоке "Возможно, вы искали"""
        first_result = self.wait.until(
            EC.element_to_be_clickable(self.TOP_RESULT)
        )
        first_result.click()

    @allure.step("Проверить, что открылась страница фильма")
    def is_film(self):
        # Ждём, пока URL изменится на страницу фильма
        return self.wait.until(EC.url_contains("/film/"))

    @allure.step("Проверить, что заголовок страницы содержит: {name}")
    def is_title_film(self, name):
        return self.wait.until(EC.title_contains(name))

    @allure.step("Перейти на страницу с билетами")
    def go_to_movie_tickets(self):
        """Переход на страницу с билетами"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.TICKET_BTN)
        )
        btn.click()
        return self.driver.title

    @allure.step("Перейти на страницу онлайн-кинотеатра")
    def go_to_online_movie(self):
        """Переход на страницу онлайн-кинотеатра"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.ONLINE_BTN)
        )
        btn.click()
        return self.driver.title

    @allure.step("Перейти на страницу магазина")
    def go_to_shop(self):
        """Переход на страницу магазина"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.SHOP_BTN)
        )
        btn.click()
        return self.driver.title

    @allure.step("Перейти на страницу 'Фильмы'")
    def go_to_films(self):
        """Переход на страницу фильмы"""
        btn = self.wait.until(
            EC.element_to_be_clickable(self.FILMS_BTN)
        )
        btn.click()
        return self.driver.title