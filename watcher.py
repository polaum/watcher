import requests
from pony.orm import *
from datetime import date

imdb_api_key = "b334d15e"

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
          'Nov': 11, 'Dec': 12}


class WatchedFilm(db.Entity):
    title = Required(str)
    year = Required(int)
    imdb_id = PrimaryKey(str)
    release_date = Required(date)


db.generate_mapping(create_tables=True)


class AlreadyWatchedException(Exception):
    pass


class Movie:
    def __init__(self, name: str):
        name = name.replace(' ', '_').lower()
        movie_data = requests.get('http://www.omdbapi.com/?t=' + name + '&apikey=' + str(imdb_api_key))
        self.all_info: dict = movie_data.json()

    @property
    def title(self) -> str:
        return str(self.all_info["Title"])

    @property
    def year(self) -> int:
        return int(self.all_info["Year"])

    @property
    def imdb_id(self) -> str:
        return str(self.all_info['imdbID'])

    @property
    def release_date(self):
        release_txt = str(self.all_info['Released'])
        release_lst = release_txt.split(" ")
        day = int(release_lst[0])
        month = int(months[release_lst[1]])
        year = int(release_lst[2])
        return date(year, month, day)

    @db_session
    def is_watched(self):
        if WatchedFilm.get(imdb_id=self.imdb_id):
            raise AlreadyWatchedException('Already watched this film!')
        return False

    @db_session
    def new_watch(self):
        if not self.is_watched():
            WatchedFilm(title=self.title, year=self.year, imdb_id=self.imdb_id, release_date=self.release_date)




