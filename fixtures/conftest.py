import pytest
from main import BooksCollector


# Фикстура для создания экземпляра BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()