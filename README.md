Кинопоиск — Автотесты UI и API
Проект автоматизированного тестирования сайта Кинопоиск (https://www.kinopoisk.ru/) и API PoiskKino (https://api.poiskkino.dev).

Тесты покрывают как UI-сценарии (поиск фильмов, навигация по вкладкам), так и API-запросы (поиск по ключевому слову, детальная информация о фильме, награды, негативные сценарии).

📋 Содержание
# Стек технологий
# Структура проекта
# Установка
# Настройка окружения
# Запуск тестов
# Allure-отчёты
# Описание тестов
# Полезные команды

# Стек технологий
Python 3.10+: Язык разработки
Pytest: Фреймворк для тестирования
Selenium WebDriver: Автоматизация браузера
Requests: HTTP-запросы к API
Allure: Формирование отчётов
python-dotenv: Загрузка переменных окружения

# Структура проекта
text
project/
│
├── pages/
│   └── ui_page.py          # Page Object для главной страницы Кинопоиска
│
├── tests/
│   ├── test_ui.py          # UI-тесты (поиск, навигация)
│   └── test_api.py         # API-тесты (поиск, фильмы, награды, негатив)
│
├── conftest.py             # Фикстуры (browser, headers)
├── .env                    # Переменные окружения (не коммитится)
├── .env.example            # Шаблон переменных окружения
├── requirements.txt        # Зависимости
├── pytest.ini              # Конфигурация Pytest
└── README.md

# Установка
1. Клонировать репозиторий
git clone https://github.com/Atallana/Diplom.git
cd Diplom
2. Создать виртуальное окружение
python -m venv .venv
Windows:
.venv\Scripts\activate
3. Установить зависимости
pip install -r requirements.txt
4. Установить Allure-pytest
pip install allure-pytest
Проверка:
allure --version

# Настройка окружения
Файл .env в корне проекта
X-API-KEY = записать свой ключ
(API-ключ получен на api.poiskkino.dev)

# Запуск тестов
- Запуск всех тестов
pytest --alluredir=allure-results
- Запуск только UI-тестов
pytest -m ui --alluredir=allure-results
- Запуск только API-тестов
pytest -m api --alluredir=allure-results

# Allure-отчёты
Генерация и открытие отчёта пошагово:
allure generate allure-results -o allure-report --clean
allure open allure-report

# Описание тестов
🖥 UI-тесты (test_ui.py)
test_search_movie_by_exact_name	
Поиск фильма «Титаник» по точному названию и проверка перехода на страницу фильма
test_go_to_movie_tickets	
Переход на вкладку «Билеты в кино»
test_go_to_online_movie	
Переход на вкладку «Онлайн-кинотеатр»
test_go_to_shop	
Переход на вкладку «Магазин»
test_go_to_films	
Переход на вкладку «Фильмы»
Page Object MainPage включает:
open_main_page() — открытие главной страницы с авто-закрытием рекламы
close_ad_if_present() — закрытие модального рекламного окна
main_search(movie_name) — ввод названия в поисковую строку
search_top_result() — выбор первого результата из блока «Возможно, вы искали»
is_film() / is_title_film() — проверки URL и title
методы навигации: go_to_movie_tickets, go_to_online_movie, go_to_shop, go_to_films

🌐 API-тесты (test_api.py)
test_search_film_by_name	GET /v1.5/keyword	Поиск «Мачеха» — непустой список docs[0].movies
test_get_movie_by_id	GET /v1.5/movie?id=435	200 + dict
test_get_movie_awards	GET /v1.5/movie/awards?movieId=326	200 + dict
test_search_with_empty_keyword	GET /v1.5/keyword?title=	200 + пустой docs
test_search_with_empty_api_key	GET /v1.5/keyword с пустым ключом	401 Unauthorized

# Полезные команды
pytest -v	Подробный вывод тестов
pytest -s	Показывать print() в консоли
pytest -x	Остановиться на первом падении
pytest -k "search"	Запустить тесты, содержащие search в имени
pytest --lf	Перезапустить только упавшие тесты
allure serve allure-results	Открыть Allure-отчёт

# Особенности
Авто-закрытие рекламы на главной странице Кинопоиска (модальное окно ReactModalPortal).
Явные ожидания (WebDriverWait) — устойчивость тестов к динамической загрузке.
Allure-шаги и вложения — детализация каждого действия и тела API-ответов.
Маркировка тестов (@pytest.mark.ui, @pytest.mark.api) — удобная фильтрация запуска.
