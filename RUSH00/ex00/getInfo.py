# OMDB API KEY : http://www.omdbapi.com/?i=tt3896198&apikey=87ac0cb0

import sys
import requests
import omdb
from django.conf import settings
import pickle
import os
import random

class moviemon:

    def __init__(self):
        "Ok on a initialise la classe moviemon"
    
    def load(self, fileName):
        nomdossiersauvegarde = "saved_game/"
        nomfichier = fileName
        nomSauvegarde = nomdossiersauvegarde + nomfichier
        self = pickle.load(open(nomfichier, 'rb'))
        return self

    
    def get_random_movie(self, moviemonListAvecDetailClean):
        randomNumber = random.randint(0, len(moviemonListAvecDetailClean) - 1)
        return moviemonListAvecDetailClean[randomNumber]
    
    def load_default_settings(self):
        API_KEY = "87ac0cb0"
        moviemonList = settings.MOVIEMON_SETTINGS[0]['IMDB_title']
        try : 
            self.position = settings.MOVIEMON_SETTINGS[0]['position_start']
            self.grid_size = settings.MOVIEMON_SETTINGS[0]['grid_size']
            # omdb.set_default('apikey', API_KEY)
            # self.moviemonListAvecDetail = []
            # for index in moviemonList: 
            #     res = omdb.get(title=moviemonList[index])
            #     self.moviemonListAvecDetail.append(res)

            # ####### TEMPS DES TESTS
            self.nombreMovieballs = 3
            self.found = 0
            self.moviedex = []
            self.moviemonListAvecDetail = [{'title': 'True Grit', 'year': '2010', 'rated': 'PG-13', 'released': '22 Dec 2010', 'runtime': '110 min', 'genre': 'Adventure, Drama, Western', 'director': 'Ethan Coen, Joel Coen', 'writer': 'Joel Coen (screenplay), Ethan Coen (screenplay), Charles Portis (novel)', 'actors': 'Jeff Bridges, Hailee Steinfeld, Matt Damon, Josh Brolin', 'plot': "A stubborn teenager enlists the help of a tough U.S. Marshal to track down her father's murderer.", 'language': 'English', 'country': 'USA', 'awards': 'Nominated for 10 Oscars. Another 37 wins & 153 nominations.', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjIxNjAzODQ0N15BMl5BanBnXkFtZTcwODY2MjMyNA@@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '7.6/10'}, {'source': 'Rotten Tomatoes', 'value': '96%'}, {'source': 'Metacritic', 'value': '80/100'}], 'metascore': '80', 'imdb_rating': '7.6', 'imdb_votes': '277,704', 'imdb_id': 'tt1403865', 'type': 'movie', 'dvd': '07 Jun 2011', 'box_office': '$171,031,347', 'production': 'Paramount Pictures', 'website': 'http://www.truegritmovie.com/', 'response': 'True'}, {'title': 'Zero', 'year': '2018', 'rated': 'N/A', 'released': '21 Dec 2018', 'runtime': '164 min', 'genre': 'Comedy, Drama, Romance', 'director': 'Aanand L. Rai', 'writer': 'Himanshu Sharma', 'actors': 'Shah Rukh Khan, Anushka Sharma, Katrina Kaif, Mohammed Zeeshan Ayyub', 'plot': 'The story revolves around Bauua Singh (Shah Rukh Khan), a vertically challenged man, who is full of charm and wit, with a pinch of arrogance. Born to a wealthy family and raised in an environment of affluence, he is challenged to broaden his horizon and find purpose in life.', 'language': 'Hindi', 'country': 'India', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzg5YjA4ZTgtZGI3MC00ODVkLTliYmEtOWQ1NTY1ODg0ZjU1XkEyXkFqcGdeQXVyNzI5NjYzODI@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.1/10'}, {'source': 'Rotten Tomatoes', 'value': '40%'}], 'metascore': 'N/A', 'imdb_rating': '6.1', 'imdb_votes': '15,618', 'imdb_id': 'tt6527426', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'Yash Raj Films USA Inc.', 'website': 'N/A', 'response': 'True'}, {'title': 'Jaguar', 'year': '1968', 'rated': 'NOT RATED', 'released': '01 Jul 1968', 'runtime': '110 min', 'genre': 'Documentary', 'director': 'Jean Rouch', 'writer': 'N/A', 'actors': 'N/A', 'plot': 'The adventures of three young men who leave their homeland Savannah, Niger, and go looking for fortune in Ghana.', 'language': 'French', 'country': 'France', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BZTQ3YjlkZDMtNzQyYi00NDRiLTg3YmItNGVmMjM1ZTg5ODU0XkEyXkFqcGdeQXVyNTcxNjk2NTk@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '7.5/10'}], 'metascore': 'N/A', 'imdb_rating': '7.5', 'imdb_votes': '174', 'imdb_id': 'tt0286727', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'N/A', 'website': 'N/A', 'response': 'True'}, {'title': 'Breathe', 'year': '2017', 'rated': 'PG-13', 'released': '27 Oct 2017', 'runtime': '118 min', 'genre': 'Biography, Drama, Romance', 'director': 'Andy Serkis', 'writer': 'William Nicholson (screenplay)', 'actors': 'Andrew Garfield, Claire Foy, Ed Speleers, Tom Hollander', 'plot': 'The inspiring true love story of Robin and Diana Cavendish, an adventurous couple who refuse to give up in the face of a devastating disease. Their heartwarming celebration of human possibility marks the directorial debut of Andy Serkis.', 'language': 'English, German, Spanish', 'country': 'UK', 'awards': '1 win & 3 nominations.', 'poster': 'https://m.media-amazon.com/images/M/MV5BMTg1OTcxNjU1MV5BMl5BanBnXkFtZTgwMzcwMTQ3MzI@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '7.1/10'}, {'source': 'Rotten Tomatoes', 'value': '67%'}, {'source': 'Metacritic', 'value': '51/100'}], 'metascore': '51', 'imdb_rating': '7.1', 'imdb_votes': '13,815', 'imdb_id': 'tt5716464', 'type': 'movie', 'dvd': '02 Jan 2018', 'box_office': '$475,685', 'production': 'Bleecker Street / Participant Media.', 'website': 'N/A', 'response': 'True'}, {'title': 'Holmes & Watson', 'year': '2018', 'rated': 'N/A', 'released': '25 Dec 2018', 'runtime': '90 min', 'genre': 'Adventure, Comedy, Crime, Mystery', 'director': 'Etan Cohen', 'writer': 'Etan Cohen, Arthur Conan Doyle (Sherlock Holmes and Dr. Watson were created by the late)', 'actors': 'Will Ferrell, Ralph Fiennes, John C. Reilly, Lauren Lapkus', 'plot': "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.", 'language': 'English', 'country': 'USA', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BZTNjMjAwNjQtYjE4MC00OGNlLTgzNDctNTE2NTBjMjRlMDgwXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '3.9/10'}, {'source': 'Rotten Tomatoes', 'value': '8%'}, {'source': 'Metacritic', 'value': '24/100'}], 'metascore': '24', 'imdb_rating': '3.9', 'imdb_votes': '1,583', 'imdb_id': 'tt1255919', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'Columbia Pictures', 'website': 'N/A', 'response': 'True'}, {'title': 'The Upside', 'year': '2017', 'rated': 'N/A', 'released': '11 Jan 2019', 'runtime': '125 min', 'genre': 'Comedy, Drama', 'director': 'Neil Burger', 'writer': 'Jon Hartmere (screenplay by), Éric Toledano (based on the motion picture "Les Intouchables" by), Olivier Nakache (based on the motion picture "Les Intouchables" by)', 'actors': 'Nicole Kidman, Kevin Hart, Bryan Cranston, Julianna Margulies', 'plot': "A comedic look at the relationship between a wealthy man with quadriplegia and an unemployed man with a criminal record who's hired to help him.", 'language': 'English', 'country': 'USA', 'awards': '2 wins.', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzY3NzYyNjI0N15BMl5BanBnXkFtZTgwNjYzMDc0NjM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '3.8/10'}, {'source': 'Metacritic', 'value': '44/100'}], 'metascore': '44', 'imdb_rating': '3.8', 'imdb_votes': '1,675', 'imdb_id': 'tt1987680', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'N/A', 'website': 'N/A', 'response': 'True'}, {'title': 'The Predator', 'year': '2018', 'rated': 'N/A', 'released': '14 Sep 2018', 'runtime': '107 min', 'genre': 'Action, Adventure, Horror, Sci-Fi, Thriller', 'director': 'Shane Black', 'writer': 'Fred Dekker, Shane Black, Jim Thomas (based on characters created by), John Thomas (based on characters created by)', 'actors': 'Boyd Holbrook, Trevante Rhodes, Jacob Tremblay, Keegan-Michael Key', 'plot': "When a young boy accidentally triggers the universe's most lethal hunters' return to Earth, only a ragtag crew of ex-soldiers and a disgruntled scientist can prevent the end of the human race.", 'language': 'English, Spanish', 'country': 'USA, Canada', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjM5MDk2NDIxMF5BMl5BanBnXkFtZTgwNjU5NDk3NTM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '5.5/10'}, {'source': 'Rotten Tomatoes', 'value': '33%'}, {'source': 'Metacritic', 'value': '48/100'}], 'metascore': '48', 'imdb_rating': '5.5', 'imdb_votes': '72,503', 'imdb_id': 'tt3829266', 'type': 'movie', 'dvd': '18 Dec 2018', 'box_office': 'N/A', 'production': '20th Century Fox', 'website': 'N/A', 'response': 'True'}, {'title': 'Bird Box', 'year': '2018', 'rated': 'N/A', 'released': '21 Dec 2018', 'runtime': '124 min', 'genre': 'Drama, Horror, Sci-Fi, Thriller', 'director': 'Susanne Bier', 'writer': 'Eric Heisserer (screenplay), Josh Malerman (novel)', 'actors': 'Sandra Bullock, Trevante Rhodes, John Malkovich, Sarah Paulson', 'plot': 'A woman and a pair of children are blindfolded and make their way through a dystopian setting.', 'language': 'English', 'country': 'USA', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjAzMTI1MjMyN15BMl5BanBnXkFtZTgwNzU5MTE2NjM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.4/10'}, {'source': 'Rotten Tomatoes', 'value': '65%'}, {'source': 'Metacritic', 'value': '53/100'}], 'metascore': '53', 'imdb_rating': '6.4', 'imdb_votes': '773', 'imdb_id': 'tt2737304', 'type': 'movie', 'dvd': '21 Dec 2018', 'box_office': 'N/A', 'production': 'Netflix', 'website': 'N/A', 'response': 'True'}, {'title': 'Halloween', 'year': '1978', 'rated': 'R', 'released': '27 Oct 1978', 'runtime': '91 min', 'genre': 'Horror, Thriller', 'director': 'John Carpenter', 'writer': 'John Carpenter (screenplay), Debra Hill (screenplay)', 'actors': 'Donald Pleasence, Jamie Lee Curtis, Nancy Kyes, P.J. Soles', 'plot': 'Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again.', 'language': 'English', 'country': 'USA', 'awards': '5 wins & 2 nominations.', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzk1OGU2NmMtNTdhZC00NjdlLWE5YTMtZTQ0MGExZTQzOGQyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '7.8/10'}, {'source': 'Rotten Tomatoes', 'value': '95%'}, {'source': 'Metacritic', 'value': '81/100'}], 'metascore': '81', 'imdb_rating': '7.8', 'imdb_votes': '199,623', 'imdb_id': 'tt0077651', 'type': 'movie', 'dvd': '27 Oct 1997', 'box_office': 'N/A', 'production': 'Compass International Pictures', 'website': 'N/A', 'response': 'True'}, {'title': 'Venom', 'year': '2018', 'rated': 'N/A', 'released': '05 Oct 2018', 'runtime': '112 min', 'genre': 'Action, Sci-Fi', 'director': 'Ruben Fleischer', 'writer': "Jeff Pinkner (screenplay by), Scott Rosenberg (screenplay by), Kelly Marcel (screenplay by), Jeff Pinkner (screen story by), Scott Rosenberg (screen story by), Todd McFarlane (Marvel's Venom Character created by), David Michelinie (Marvel's Venom Character created by)", 'actors': 'Tom Hardy, Michelle Williams, Riz Ahmed, Scott Haze', 'plot': 'When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego "Venom" to save his life.', 'language': 'English', 'country': 'USA, China', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.8/10'}, {'source': 'Metacritic', 'value': '35/100'}], 'metascore': '35', 'imdb_rating': '6.8', 'imdb_votes': '205,968', 'imdb_id': 'tt1270797', 'type': 'movie', 'dvd': '18 Jun 2013', 'box_office': 'N/A', 'production': 'Vis', 'website': 'N/A', 'response': 'True'}]
            # print(self.position)
            # print(self.grid_size)
            # print(self.nombreMovieballs)
            # print(self.moviemonListAvecDetail)
        except Exception as e:
            print(e)
        return self

    def get_strength(self):
        return len(self.moviedex)
    
    def get_movie(self, moviemonId):
        for moviemon in self.moviemonListAvecDetail:
            if (moviemon['imdb_id'] == moviemonId):
                moviemonDetail = {
                    'nom' : moviemon['title'],
                    'poster' : moviemon['poster'],
                    'realisateur' : moviemon['director'],
                    'annee' : moviemon['year'],
                    'rating' : moviemon['imdb_rating'],
                    'synopsis': moviemon['plot'],
                    'acteurs' : moviemon['actors'],
                }
                return moviemonDetail
        return ""

    def save(self, fileName):
        nomdossiersauvegarde = "saved_game/"
        if not os.path.exists(nomdossiersauvegarde):
            os.makedirs(nomdossiersauvegarde)
        nomfichier = fileName
        nomSauvegarde = nomdossiersauvegarde + nomfichier
        os.system("touch " + nomSauvegarde)
        pickle.dump(self, open(nomSauvegarde, 'wb'))
        return self

    def saveTMP(self):
        nomdossiersauvegarde = "saved_game/"
        if not os.path.exists(nomdossiersauvegarde):
            os.makedirs(nomdossiersauvegarde)
        pickle.dump(self, open(nomdossiersauvegarde + "mypicklefile.txt", 'wb'))
        return self

    def dump(self):
        nomdossiersauvegarde = "saved_game/"
        moviemongame = pickle.load(open(nomdossiersauvegarde + 'mypicklefile.txt', 'rb'))
        return moviemongame
    

# if __name__ == '__main__':
#     try:
#         newmoviemon = moviemon()
#         newmoviemon.load_default_settings()
#         newmoviemon.get_movie("True Grit")
#         test = [
#             {'title': 'Holmes & Watson', 'year': '2018', 'rated': 'N/A', 'released': '25 Dec 2018', 'runtime': '90 min', 'genre': 'Adventure, Comedy, Crime, Mystery', 'director': 'Etan Cohen', 'writer': 'Etan Cohen, Arthur Conan Doyle (Sherlock Holmes and Dr. Watson were created by the late)', 'actors': 'Will Ferrell, Ralph Fiennes, John C. Reilly, Lauren Lapkus', 'plot': "A humorous take on Sir Arthur Conan Doyle's classic mysteries featuring Sherlock Holmes and Doctor Watson.", 'language': 'English', 'country': 'USA', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BZTNjMjAwNjQtYjE4MC00OGNlLTgzNDctNTE2NTBjMjRlMDgwXkEyXkFqcGdeQXVyMTYzMDM0NTU@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '3.9/10'}, {'source': 'Rotten Tomatoes', 'value': '8%'}, {'source': 'Metacritic', 'value': '24/100'}], 'metascore': '24', 'imdb_rating': '3.9', 'imdb_votes': '1,583', 'imdb_id': 'tt1255919', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'Columbia Pictures', 'website': 'N/A', 'response': 'True'}, {'title': 'The Upside', 'year': '2017', 'rated': 'N/A', 'released': '11 Jan 2019', 'runtime': '125 min', 'genre': 'Comedy, Drama', 'director': 'Neil Burger', 'writer': 'Jon Hartmere (screenplay by), Éric Toledano (based on the motion picture "Les Intouchables" by), Olivier Nakache (based on the motion picture "Les Intouchables" by)', 'actors': 'Nicole Kidman, Kevin Hart, Bryan Cranston, Julianna Margulies', 'plot': "A comedic look at the relationship between a wealthy man with quadriplegia and an unemployed man with a criminal record who's hired to help him.", 'language': 'English', 'country': 'USA', 'awards': '2 wins.', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzY3NzYyNjI0N15BMl5BanBnXkFtZTgwNjYzMDc0NjM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '3.8/10'}, {'source': 'Metacritic', 'value': '44/100'}], 'metascore': '44', 'imdb_rating': '3.8', 'imdb_votes': '1,675', 'imdb_id': 'tt1987680', 'type': 'movie', 'dvd': 'N/A', 'box_office': 'N/A', 'production': 'N/A', 'website': 'N/A', 'response': 'True'}, {'title': 'The Predator', 'year': '2018', 'rated': 'N/A', 'released': '14 Sep 2018', 'runtime': '107 min', 'genre': 'Action, Adventure, Horror, Sci-Fi, Thriller', 'director': 'Shane Black', 'writer': 'Fred Dekker, Shane Black, Jim Thomas (based on characters created by), John Thomas (based on characters created by)', 'actors': 'Boyd Holbrook, Trevante Rhodes, Jacob Tremblay, Keegan-Michael Key', 'plot': "When a young boy accidentally triggers the universe's most lethal hunters' return to Earth, only a ragtag crew of ex-soldiers and a disgruntled scientist can prevent the end of the human race.", 'language': 'English, Spanish', 'country': 'USA, Canada', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjM5MDk2NDIxMF5BMl5BanBnXkFtZTgwNjU5NDk3NTM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '5.5/10'}, {'source': 'Rotten Tomatoes', 'value': '33%'}, {'source': 'Metacritic', 'value': '48/100'}], 'metascore': '48', 'imdb_rating': '5.5', 'imdb_votes': '72,503', 'imdb_id': 'tt3829266', 'type': 'movie', 'dvd': '18 Dec 2018', 'box_office': 'N/A', 'production': '20th Century Fox', 'website': 'N/A', 'response': 'True'}, {'title': 'Bird Box', 'year': '2018', 'rated': 'N/A', 'released': '21 Dec 2018', 'runtime': '124 min', 'genre': 'Drama, Horror, Sci-Fi, Thriller', 'director': 'Susanne Bier', 'writer': 'Eric Heisserer (screenplay), Josh Malerman (novel)', 'actors': 'Sandra Bullock, Trevante Rhodes, John Malkovich, Sarah Paulson', 'plot': 'A woman and a pair of children are blindfolded and make their way through a dystopian setting.', 'language': 'English', 'country': 'USA', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BMjAzMTI1MjMyN15BMl5BanBnXkFtZTgwNzU5MTE2NjM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.4/10'}, {'source': 'Rotten Tomatoes', 'value': '65%'}, {'source': 'Metacritic', 'value': '53/100'}], 'metascore': '53', 'imdb_rating': '6.4', 'imdb_votes': '773', 'imdb_id': 'tt2737304', 'type': 'movie', 'dvd': '21 Dec 2018', 'box_office': 'N/A', 'production': 'Netflix', 'website': 'N/A', 'response': 'True'}, {'title': 'Halloween', 'year': '1978', 'rated': 'R', 'released': '27 Oct 1978', 'runtime': '91 min', 'genre': 'Horror, Thriller', 'director': 'John Carpenter', 'writer': 'John Carpenter (screenplay), Debra Hill (screenplay)', 'actors': 'Donald Pleasence, Jamie Lee Curtis, Nancy Kyes, P.J. Soles', 'plot': 'Fifteen years after murdering his sister on Halloween night 1963, Michael Myers escapes from a mental hospital and returns to the small town of Haddonfield, Illinois to kill again.', 'language': 'English', 'country': 'USA', 'awards': '5 wins & 2 nominations.', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzk1OGU2NmMtNTdhZC00NjdlLWE5YTMtZTQ0MGExZTQzOGQyXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '7.8/10'}, {'source': 'Rotten Tomatoes', 'value': '95%'}, {'source': 'Metacritic', 'value': '81/100'}], 'metascore': '81', 'imdb_rating': '7.8', 'imdb_votes': '199,623', 'imdb_id': 'tt0077651', 'type': 'movie', 'dvd': '27 Oct 1997', 'box_office': 'N/A', 'production': 'Compass International Pictures', 'website': 'N/A', 'response': 'True'}, {'title': 'Venom', 'year': '2018', 'rated': 'N/A', 'released': '05 Oct 2018', 'runtime': '112 min', 'genre': 'Action, Sci-Fi', 'director': 'Ruben Fleischer', 'writer': "Jeff Pinkner (screenplay by), Scott Rosenberg (screenplay by), Kelly Marcel (screenplay by), Jeff Pinkner (screen story by), Scott Rosenberg (screen story by), Todd McFarlane (Marvel's Venom Character created by), David Michelinie (Marvel's Venom Character created by)", 'actors': 'Tom Hardy, Michelle Williams, Riz Ahmed, Scott Haze', 'plot': 'When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego "Venom" to save his life.', 'language': 'English', 'country': 'USA, China', 'awards': 'N/A', 'poster': 'https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_SX300.jpg', 'ratings': [{'source': 'Internet Movie Database', 'value': '6.8/10'}, {'source': 'Metacritic', 'value': '35/100'}], 'metascore': '35', 'imdb_rating': '6.8', 'imdb_votes': '205,968', 'imdb_id': 'tt1270797', 'type': 'movie', 'dvd': '18 Jun 2013', 'box_office': 'N/A', 'production': 'Vis', 'website': 'N/A', 'response': 'True'}
#         ]
#         newmoviemon.get_random_movie(test)
#         # newmoviemon.saveTMP()
#         # newmoviemon.save(1,2000)
#         # newmoviemon.load(1,2000)


#     except Exception as e:
#         print(e)