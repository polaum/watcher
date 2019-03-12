import requests
from datetime import date

imdb_api_key = "b334d15e"

months = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10,
          'Nov': 11, 'Dec': 12}

watched_films = []


class Movie():
    def __init__(self, name: str):
        name = name.replace(' ', '_')
        name = name.lower()
        movie_data = requests.get('http://www.omdbapi.com/?t=' + name + '&apikey=' + str(imdb_api_key))
        self.all_info: dict = movie_data.json()

    @property
    def title(self) -> str:
        return str(self.all_info["Title"])

    @property
    def year(self) -> int:
        return int(self.all_info["Year"])

    @property
    def release_date(self):
        release_txt = str(self.all_info['Released'])
        release_lst = release_txt.split(" ")
        day = int(release_lst[0])
        month = int(months[release_lst[1]])
        year = int(release_lst[2])
        return date(year, month, day)

    def watched(self):
        if self.title in watched_films:
            print("Already watched this film!")
        else:
            watched_films.append(self.title)
            print("Successfully added {film_name} to your watched list!".format(film_name=self.title))

