#!/usr/bin/python
"""
Grab the name of a rock band.
"""

'''
Fix the error (see screenshots) when the index is out of range.
'''

import urllib
from random import choice # to choose a random item from a list
from bs4 import BeautifulSoup
#from xml.etree.ElementTree import parse
from config import debug


'''
another API: http://www.last.fm/api

Documentation: http://developer.echonest.com/docs/v4/artist.html#search

'''

class rockBand ( object ) :
	def __init__ ( self ) :
		True

	def getName ( self ) :
	
		api_key = 'api_key=AU1JLQPY2FQCSHJHH'
		
		format = 'format=xml'
	
		url_base = 'http://developer.echonest.com/api/v4/' 
		
		genre_listing_url = url_base + 'genre/list?' + '&'.join ( ( api_key, format ) )
			
		#genre_parameters = ( )
		
		sock = urllib.urlopen ( genre_listing_url )
		
		XMLSource = sock.read ( )
		
		sock.close()
		
		rockBandXML = BeautifulSoup(XMLSource)
		
		genres = rockBandXML.find_all('name')
		
		# grab a random genre; 898 were returned the last time I ran this query on Feb 25
		random_genre = choice ( genres )
		
		sort_parameters = ( 'familiarity-asc', 'hotttnesss-asc', 'familiarity-desc', 'hotttnesss-desc', 'artist_start_year-asc', 'artist_start_year-desc', 'artist_end_year-asc', 'artist_end_year-desc' )
		
		sort = 'sort=' + choice ( sort_parameters )

		results = 'results=100'
		
		start = 'start=' + choice ( ('0', '15', '30') )
		
		genre = 'genre=' + random_genre.text

		artist_search_url = url_base + 'artist/search?' + '&'.join ( ( api_key, genre, results, start, sort, format ) )
		
		# FIXME: format this correctly
		
		sock = urllib.urlopen ( artist_search_url )

		XMLSource = sock.read ( )
		
		sock.close()
		
		# FIXME: need to be sure we're returning something and not raising errors!
		
		rockBandNamesXML = BeautifulSoup(XMLSource)

		bands = rockBandNamesXML.find_all('name')

		random_band = choice ( bands ) 
	
		return random_band.text
		#True

'''

http://developer.echonest.com/api/v4/artist/biographies?api_key=AU1JLQPY2FQCSHJHH&id=ARH6W4X1187B99274F&format=xml&results=1&start=0&license=cc-by-sa


search by name:
http://developer.echonest.com/api/v4/artist/search?api_key=AU1JLQPY2FQCSHJHH&name=blue&format=xml&results=1&start=0


search by genre:
http://developer.echonest.com/api/v4/artist/search?api_key=AU1JLQPY2FQCSHJHH&genre=metal&format=xml


can control the familiarity of the artist via the 'familiarity' parameter.

can control the years of the artist via 'artist_start_year_before'

sort parameters:


list genres:

http://developer.echonest.com/api/v4/genre/list?api_key=AU1JLQPY2FQCSHJHH&format=xml

'''

