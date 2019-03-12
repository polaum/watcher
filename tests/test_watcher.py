from datetime import date
from watcher import Movie, watched_films


def test_movie_title_test():
    movie1= Movie('mary poppins')
    assert movie1.title == 'Mary Poppins'


def test_movie_date():
    movie1= Movie('mary poppins')
    assert movie1.release_date == date(1964, 12, 3)


def test_movie_year():
    movie1=Movie('mary poppins')
    assert movie1.year == 1964


def test_watched():
    watched_films_num = len(watched_films)
    movie1 = Movie('mary poppins')
    movie1.watched()
    assert len(watched_films) == watched_films_num + 1


def test_already_watched():
    watched_films_num = len(watched_films)
    movie1 = Movie('mary poppins')
    movie1.watched()
    assert len(watched_films) == watched_films_num
