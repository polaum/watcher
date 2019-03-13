import pytest
from datetime import date
from watcher import Movie, AlreadyWatchedException


def test_movie_title():
    movie1 = Movie('mary poppins')
    assert movie1.title == 'Mary Poppins'


def test_movie_date():
    movie1 = Movie('mary poppins')
    assert movie1.release_date == date(1964, 12, 3)


def test_imdb_id():
    movie1 = Movie('mary poppins')
    assert movie1.imdb_id == "tt0058331"


def test_movie_year():
    movie1 = Movie('mary poppins')
    assert movie1.year == 1964


def test_new_watch():
    movie1 = Movie('mary poppins')
    movie1.new_watch()


def test_already_watched():
    movie1 = Movie('mary poppins')
    with pytest.raises(AlreadyWatchedException):
        movie1.new_watch()
