import pytest, random
from datetime import date
from watcher import Movie, AlreadyWatchedException, WatchedFilm

movies = ['mary poppins', 'Aquaman', 'Cinderella', 'Pretty Woman']
opt = len(movies) - 1


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
    movie_name = movies[random.randint(0, opt)]
    movie1 = Movie(movie_name)
    if movie1.is_watched:
        with pytest.raises(AlreadyWatchedException):
            movie1.new_watch()
    else:
        movie1.new_watch()
        assert WatchedFilm.get(imdb_id=movie1.imdb_id) == True


def test_already_watched():
    movie1 = Movie('mary poppins')
    with pytest.raises(AlreadyWatchedException):
        movie1.new_watch()
