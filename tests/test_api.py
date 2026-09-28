import os
import allure
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('X-API-KEY')
url = ("https://api.poiskkino.dev")

@pytest.fixture
def headers():
    """Стандартные заголовки для API Кинопоиска."""
    return {
        'accept': 'application/json',
        'X-API-KEY': key
    }


def attach_response(response):
    """Прикрепляем тело ответа к Allure-отчёту."""
    allure.attach(
        response.text,
        name="response_body",
        attachment_type=allure.attachment_type.JSON,
    )

@pytest.mark.api
@allure.feature("API: Поиск")
@allure.story("Поиск по ключевому слову")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Поиск фильма на русском языке")
@allure.description("Проверяем, что поиск по названию 'Мачеха' возвращает непустой список фильмов.")
def test_search_film_by_name(headers):
    name = 'Мачеха'

    with allure.step(f"Отправляем GET /v1.5/keyword?title={name}"):
        response = requests.get(
            f"{url}/v1.5/keyword",
            params={"title": name},
            headers=headers,
        )
        attach_response(response)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200, \
            f"Ожидали 200, получили {response.status_code}: {response.text}"

    with allure.step("Проверяем, что ответ — словарь"):
        resp = response.json()
        assert isinstance(resp, dict), f"Ожидали dict, получили {type(resp)}"

    with allure.step("Проверяем, что в ответе есть непустой список docs"):
        assert "docs" in resp, "В ответе нет ключа 'docs'"
        assert len(resp["docs"]) > 0, "Список 'docs' пуст"

    with allure.step("Проверяем, что у первого документа есть непустой список movies"):
        doc = resp["docs"][0]
        assert "movies" in doc, "У документа нет ключа 'movies'"
        movies = doc["movies"]
        assert isinstance(movies, list), f"'movies' не список, а {type(movies)}"
        assert len(movies) > 0, "Список 'movies' пуст"


@pytest.mark.api
@allure.feature("API: Фильмы")
@allure.story("Детальная информация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Получение детальной информации о фильме по ID")
@allure.description("Проверяем, что GET /v1.5/movie?id=435 возвращает 200 и словарь.")
def test_get_movie_by_id(headers):
    movie_id = 435

    with allure.step(f"Отправляем GET /v1.5/movie?id={movie_id}"):
        response = requests.get(
            f"{url}/v1.5/movie",
            params={"id": movie_id},
            headers=headers,
        )
        attach_response(response)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200, \
            f"Ожидали 200, получили {response.status_code}: {response.text}"

    with allure.step("Проверяем, что ответ — словарь"):
        assert isinstance(response.json(), dict)


@pytest.mark.api
@allure.feature("API: Фильмы")
@allure.story("Награды")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Получение списка наград фильма")
@allure.description("Проверяем, что GET /v1.5/movie/awards?movieId=326 возвращает 200 и словарь.")
def test_get_movie_awards(headers):
    movie_id = 326

    with allure.step(f"Отправляем GET /v1.5/movie/awards?movieId={movie_id}"):
        response = requests.get(
            f"{url}/v1.5/movie/awards",
            params={"movieId": movie_id},
            headers=headers,
        )
        attach_response(response)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200, \
            f"Ожидали 200, получили {response.status_code}: {response.text}"

    with allure.step("Проверяем, что ответ — словарь"):
        assert isinstance(response.json(), dict)


@pytest.mark.api
@allure.feature("API: Негативные сценарии")
@allure.story("Пустые параметры")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Поиск по пустому ключевому слову")
@allure.description("Проверяем, что GET /v1.5/keyword с пустым title возвращает 200 и пустой список docs.")
def test_search_with_empty_keyword(headers):
    with allure.step("Отправляем GET /v1.5/keyword?title=''"):
        response = requests.get(
            f"{url}/v1.5/keyword",
            params={"title": ""},
            headers=headers,
        )
        attach_response(response)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200, \
            f"Ожидали 200, получили {response.status_code}: {response.text}"

    with allure.step("Проверяем, что ответ — словарь и docs пуст"):
        resp = response.json()
        assert isinstance(resp, dict)
        assert resp.get("docs") == [], f"Ожидали пустой docs, получили {resp.get('docs')}"


@pytest.mark.api
@allure.feature("API: Негативные сценарии")
@allure.story("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Запрос с пустым API-ключом")
@allure.description("Проверяем, что запрос с пустым X-API-KEY возвращает 401.")
def test_search_with_empty_api_key():
    empty_headers = {
        'accept': 'application/json',
        'X-API-KEY': ""   # пустая строка, а не пробел
    }

    with allure.step("Отправляем GET /v1.5/keyword?title=Мачеха с пустым X-API-KEY"):
        response = requests.get(
            f"{url}/v1.5/keyword",
            params={"title": "Мачеха"},
            headers=empty_headers,
        )
        attach_response(response)

    with allure.step("Проверяем статус-код 401"):
        assert response.status_code == 401, \
            f"Ожидали 401, получили {response.status_code}: {response.text}"

    with allure.step("Проверяем, что ответ — словарь"):
        assert isinstance(response.json(), dict)
