# OMDB API KEY : http://www.omdbapi.com/?i=tt3896198&apikey=87ac0cb0

import sys
import requests
import omdb
from settings import MOVIEMON_SETTINGS

class moviemon:

    def __init__(self):
        "Ok on a initialise la classe"
    
    def load(self, donnees):
        return
    
    def get_random_movie(self, moviemonListAvecDetail):
        return
    
    def load_default_settings(self):
        API_KEY = "87ac0cb0"
        moviemonList = MOVIEMON_SETTINGS[0]['IMDB_title']
        try : 
            omdb.set_default('apikey', API_KEY)
            self.moviemonListAvecDetail = []
            for index in moviemonList: 
                res = omdb.get(title=moviemonList[index])
                self.moviemonListAvecDetail.append(res)
            print(self.moviemonListAvecDetail)
        except Exception as e:
            print(e)
        return self

    def get_strength(self):
        return
    
    def get_movie(self, moviemonName):
        return self.moviemonListAvecDetail[moviemonName]

if __name__ == '__main__':
    try:
        newmoviemon = moviemon()
        newmoviemon.load_default_settings()

    except Exception as e:
        print(e)
