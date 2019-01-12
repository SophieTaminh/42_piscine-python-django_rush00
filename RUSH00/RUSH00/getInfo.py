# OMDB API KEY : http://www.omdbapi.com/?i=tt3896198&apikey=87ac0cb0

import sys
import requests
import omdb
from settings import MOVIEMON_SETTINGS
import pickle

class moviemon:

    def __init__(self):
        "Ok on a initialise la classe moviemon"
    
    def load(self, position, nombreMovieballs, moviedex):
        self.position = position
        self.nombreMovieballs = nombreMovieballs
        self.moviedex = moviedex
        return self
    
    def get_random_movie(self, moviemonListAvecDetail, moviemonDex):
        return
    
    def load_default_settings(self):
        # API_KEY = "87ac0cb0"
        # moviemonList = MOVIEMON_SETTINGS[0]['IMDB_title']
        try : 
            self.position = MOVIEMON_SETTINGS[0]['position_start']
            self.grid_size = MOVIEMON_SETTINGS[0]['grid_size']
            # omdb.set_default('apikey', API_KEY)
            # self.moviemonListAvecDetail = []
            # for index in moviemonList: 
            #     res = omdb.get(title=moviemonList[index])
            #     self.moviemonListAvecDetail.append(res)

            # ####### TEMPS DES TESTS
            self.nombreMovieballs = 3
            self.moviedex = []
            self.moviemonListAvecDetail = [{'title': 'True Grit', 'year': '2010', 'rated': 'PG-13', 'released': '22 Dec 2010', 'runtime': '110 min', 'genre': 'Adventure, Drama, Western', 'director': 'Ethan Coen, Joel Coen', 'writer': 'Joel Coen (screenplay), Ethan Coen (screenplay), Charles Portis (novel)', 'actors': 'Jeff Bridges, Hailee Steinfeld, Matt Damon, Josh Brolin', 'plot': "A stubborn teenager enlists the help of a tough U.S. Marshal to track down her father's murderer.", 'language': 'English', 'country': 'USA', 'awards': 'Nominated for 10 Oscars. Another 37 wins & 153 nominations.', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjIxNjAzODQ0N15BMl5BanBnXkFtZTcwODY2MjMyNA@@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '7.6/10'}, {'source': 'Rotten Tomatoes', 'value': '96%'}, {'source': 'Metacritic', 'value': '80/100'}], 'metascore': '80', 'imdb_rating': '7.6', 'imdb_votes': '277,704', 'imdb_id': 'tt1403865', 'type': 'movie', 'dvd': '07 Jun 2011', 'box_office': '$171,031,347', 'production': 'Paramount Pictures', 'website': 'http://www.truegritmovie.com/', 'response': 'True'}, {'title': 'Sinbad: The Fifth Voyage', 'year': '2014', 'rated': 'PG-13', 'released': '07 Feb 2014', 'runtime': '89 min', 'genre': 'Action, Adventure, Fantasy', 'director': 'Shahin Sean Solimon', 'writer': 'Shahin Sean Solimon, Evelyn Gabai', 'actors': 'Patrick Stewart, Lorna Raver, Isaac C. Singleton Jr., Sadie Alexandru', 'plot': "When the Sultan's first born is taken by an evil sorcerer, Sinbad is tasked with traveling to a desert of magic and creatures to save her.", 'language': 'English', 'country': 'USA', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTk2MTc5ODM0Nl5BMl5BanBnXkFtZTgwMDkwMTA5MjE@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '5.3/10'}], 'metascore': 'N/A', 'imdb_rating': '5.3', 'imdb_votes': '4,516', 'imdb_id': 'tt1403862', 'type': 'movie', 'dvd': '03 Feb 2015', 'box_office': 'N/A', 'production': 'Giant Flick', 'website': 'http://www.sinbadthemovie.com/', 'response': 'True'}, {}, {}, {'title': 'Marlene Dietrich', 'year': '2015', 'rated': 'N/A', 'released': 'N/A', 'runtime': 'N/A', 'genre': 'Biography', 'director': 'N/A', 'writer': 'N/A', 'actors': 'N/A', 'plot': 'One of the most famous divas in the cinema of the 1900s.', 'language': 'N/A', 'country': 'N/A', 'awards': 'N/A', 'poster': 'N/A', 'ratings': [], 'metascore': 'N/A', 'imdb_rating': 'N/A', 'imdb_votes': 'N/A', 'imdb_id': 'tt3357910', 'type': 'series', 'total_seasons': 'N/A', 'response': 'True'}, {}, {'title': 'Joan Crawford: The Ultimate Movie Star', 'year': '2002', 'rated': 'UNRATED', 'released': '01 Aug 2002', 'runtime': '87 min', 'genre': 'Documentary', 'director': 'Peter Fitzgerald', 'writer': 'Peter Fitzgerald', 'actors': 'Anjelica Huston, Diane Baker, Charles Busch, Ben Cooper', 'plot': 'In this documentary on the life of \'Joan Crawford\', we learn why she should be remembered as the great actress she was, and not only as the "mommie dearest." caricature she has become. ...', 'language': 'English', 'country': 'USA', 'awards': 'N/A', 'poster': 'N/A', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.2/10'}], 'metascore': 'N/A', 'imdb_rating': '6.2', 'imdb_votes': '351', 'imdb_id': 'tt0329241', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'Fitzfilm', 'website': 'N/A', 'response': 'True'}, {'title': 'Alfred the Great', 'year': '1969', 'rated': 'M', 'released': '01 Oct 1969', 'runtime': '122 min', 'genre': 'Drama, History, War', 'director': 'Clive Donner', 'writer': 'James R. Webb (story), Ken Taylor (screenplay), James R. Webb (screenplay)', 'actors': 'David Hemmings, Michael York, Prunella Ransome, Colin Blakely', 'plot': 'While Old England is being ransacked by roving Danes in the ninth century, Alfred is planning to join the priesthood. But observing the rape of his land, he puts away his religious vows, to...', 'language': 'English', 'country': 'UK', 'awards': 'N/A', 'poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4MzIzMDM0NV5BMl5BanBnXkFtZTcwNjc3ODAzMQ@@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.4/10'}], 'metascore': 'N/A', 'imdb_rating': '6.4', 'imdb_votes': '812', 'imdb_id': 'tt0064000', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'MGM', 'website': 'N/A', 'response': 'True'}, {'title': 'Aamiainen motellissa', 'year': '1966', 'rated': 'N/A', 'released': '03 Sep 1966', 'runtime': '50 min', 'genre': 'Comedy', 'director': 'Veikko Kerttula', 'writer': 'Miodrag Djurdjevic, Eila Raisalo (translation: Finnish)', 'actors': 'Esko Mattila, Kerttu Krohn, Ossi Elstelä, Saara Pakkasvirta', 'plot': 'N/A', 'language': 'Finnish', 'country': 'Finland', 'awards': 'N/A', 'poster': 'N/A', 'ratings': [], 'metascore': 'N/A', 'imdb_rating': 'N/A', 'imdb_votes': 'N/A', 'imdb_id': 'tt1403844', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'N/A', 'website': 'N/A', 'response': 'True'}, {}]
            print(self.position)
            print(self.grid_size)
            print(self.nombreMovieballs)
            print(self.moviemonListAvecDetail)
        except Exception as e:
            print(e)
         
        return self

    def get_strength(self):
        return 
    
    def get_movie(self, moviemonName):
        return 

if __name__ == '__main__':
    try:
        newmoviemon = moviemon()
        newmoviemon.load_default_settings()

    except Exception as e:
        print(e)
