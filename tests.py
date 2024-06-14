import pytest
from fixtures.conftest import collector

class TestBooksCollector:
    valid_books_list = [
        ['Мастер и Маргарита', 'Фантастика'],
        ['Ходячий замок', 'Мультфильмы']
    ]

    books_list_without_age_rating = [
        ['Мастер и Маргарита', 'Фантастика'],
        ['Ходячий замок', 'Мультфильмы']
    ]

    valid_length_book = ['Чародейки', 'Обыкновенное чудо']

    def test_add_new_book_add_one_book_positive_result(self, collector):
        collector.add_new_book(self.valid_length_book[0])
        assert self.valid_length_book[0] in collector.get_books_genre()

    @pytest.mark.parametrize('name, genre', valid_books_list)
    def test_set_book_genre_set_valid_value_genre_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name, genre', valid_books_list)
    def test_get_books_with_specific_genre_valid_genre_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_with_specific_genre(genre) == [name]


    @pytest.mark.parametrize("name, genre", books_list_without_age_rating)
    def test_get_books_for_children_return_books_for_children_list_positive_result(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == [name]

    def test_get_books_for_children_genre_age_rating_returned_list_is_empty(self, collector):
        horror_book = ["Заклятие", "Ужасы"]
        collector.add_new_book(horror_book[0])
        collector.set_book_genre(horror_book[0], horror_book[1])
        assert collector.get_books_for_children() == []

    @pytest.mark.parametrize("name", valid_length_book)
    def test_add_book_in_favorites_add_valid_value_positive_result(self, name, collector):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_add_duplicate_quantity_not_increased(self, collector):
        collector.add_new_book(self.valid_length_book[0])
        collector.add_book_in_favorites(self.valid_length_book[0])
        collector.add_book_in_favorites(self.valid_length_book[0])
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_in_favorites_positive_result(self, collector):
        collector.add_new_book(self.valid_length_book[0])
        collector.add_book_in_favorites(self.valid_length_book[0])
        collector.delete_book_from_favorites(self.valid_length_book[0])
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_favorites_list_not_empty_positive_result(self, collector):
        collector.add_new_book(self.valid_length_book[0])
        collector.add_book_in_favorites(self.valid_length_book[0])
        assert collector.get_list_of_favorites_books() == [self.valid_length_book[0]]

    def test_get_list_of_favorites_books_empty_list_positive_result(self, collector):
        assert collector.get_list_of_favorites_books() == []


