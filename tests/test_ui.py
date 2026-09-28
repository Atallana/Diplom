import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.ui_page import MainPage
import allure


@allure.feature("Поиск фильма")
@allure.story("Поиск по названию")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Поиск фильма по точному названию")
@allure.description("""
Тест проверяет поиск фильма по точному названию на главной странице Кинопоиска.
Шаги:
1. Открыть главную страницу
2. Ввести название фильма в поисковую строку
3. Перейти к первому результату поиска
4. Проверить, что открылась страница фильма
5. Проверить, что в заголовке страницы есть название фильма
""")
def test_search_movie_by_exact_name(browser):
    """Тест для поиска фильма по точному названию"""
    movie_name = "Титаник"
    main = MainPage(browser)

    with allure.step("Открываем главную страницу"):
        main.open_main_page()

    with allure.step(f"Вводим название фильма «{movie_name}» в поисковую строку"):
        main.main_search(movie_name)

    with allure.step("Переходим к первому результату поиска"):
        main.search_top_result()

    with allure.step("Проверяем, что открылась страница фильма"):
        assert main.is_film(), "Не открылась страница фильма"

    with allure.step(f"Проверяем, что в заголовке страницы есть «{movie_name}»"):
        assert main.is_title_film(movie_name), f"Ожидали {movie_name} в title"


@pytest.mark.ui
@allure.feature("Навигация")
@allure.story("Переходы по вкладкам")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Переход на вкладку «Билеты в кино»")
@allure.description("Проверка перехода на вкладку «Билеты в кино» на Кинопоиске")
def test_go_to_movie_tickets(browser):
    """Тест для проверки перехода на вкладку «Билеты в кино» на Кинопоиске"""
    main_page = MainPage(browser)

    with allure.step("Переход на главную страницу"):
        main_page.open_main_page()

    with allure.step("Выполняем переход на вкладку «Билеты в кино»"):
        response = main_page.go_to_movie_tickets()

    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Билеты в кино" in response, \
            f"Ожидали 'Билеты в кино' в заголовке, получили: {response}"


@pytest.mark.ui
@allure.feature("Навигация")
@allure.story("Переходы по вкладкам")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Переход на вкладку «Онлайн-кинотеатр»")
@allure.description("Проверка перехода на вкладку «Онлайн-кинотеатр» на Кинопоиске")
def test_go_to_online_movie(browser):
    """Тест для проверки перехода на вкладку «Онлайн-кинотеатр»"""
    main_page = MainPage(browser)

    with allure.step("Переход на главную страницу"):
        main_page.open_main_page()

    with allure.step("Выполняем переход на вкладку «Онлайн-кинотеатр»"):
        response = main_page.go_to_online_movie()

    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Онлайн кинотеатр" in response, \
            f"Ожидали 'Онлайн кинотеатр' в заголовке, получили: {response}"


@pytest.mark.ui
@allure.feature("Навигация")
@allure.story("Переходы по вкладкам")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Переход на вкладку «Магазин»")
@allure.description("Проверка перехода на вкладку «Магазин» на Кинопоиске")
def test_go_to_shop(browser):
    """Тест для проверки перехода на вкладку «Магазин»"""
    main_page = MainPage(browser)

    with allure.step("Переход на главную страницу"):
        main_page.open_main_page()

    with allure.step("Выполняем переход на вкладку «Магазин»"):
        response = main_page.go_to_shop()

    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Кинопоиск. Онлайн кинотеатр" in response, \
            f"Ожидали 'Кинопоиск. Онлайн кинотеатр' в заголовке, получили: {response}"


@pytest.mark.ui
@allure.feature("Навигация")
@allure.story("Переходы по вкладкам")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Переход на вкладку «Фильмы»")
@allure.description("Проверка перехода на вкладку «Фильмы» на Кинопоиске")
def test_go_to_films(browser):
    """Тест для проверки перехода на вкладку «Фильмы»"""
    main_page = MainPage(browser)

    with allure.step("Переход на главную страницу"):
        main_page.open_main_page()

    with allure.step("Выполняем переход на вкладку «Фильмы»"):
        response = main_page.go_to_films()

    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Фильмы" in response, \
            f"Ожидали 'Фильмы' в заголовке, получили: {response}"
