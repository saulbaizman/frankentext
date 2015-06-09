#!/usr/bin/python
"""
Grab the name of an adult movie from the adult movie database.
"""
#import urllib
from random import choice # to choose a random item from a list
#from bs4 import BeautifulSoup
import re
from config import debug


class xxxFilm ( object ) :
	def __init__ ( self ) :
		True
		
	def hasObviousWords ( self, potential_xxx_title_words ) :
		contains_obvious_word = False
		obvious_words = [ 'Cum', 'Ass', '(GAY)', 'Cock', 'Pussy', 'Sex', 'cum', 'Cunt', 'Porno', 'Orgy' ]
		for word in obvious_words :
			if word in potential_xxx_title_words :
				contains_obvious_word = True
				break
		return contains_obvious_word

	def getName ( self ) :

		iafd_search_url = 'http://www.iafd.com/results.asp?SearchType=title&searchString=the'
		
		iafd_search_results = 'iafd-search-results.html' 
		'''
		need to create a list of words that the titles do NOT contain
		pussy, dick, sex?, adult, baby, cream, erotic, xxx, '(GAY)', gangbang, numbers, tits, porn, porno, cock, 
		
		'''	
		
		'''
		FIXME: this is going to take too long to load!
		Could it cache them at the start of the game?
		'''
		
		'''
		socket = urllib.urlopen ( iafd_search_url )
		
		HTMLSource = socket.read ( )
		
		socket.close ( )
		'''
		
		'''
		>>> pattobj = re.compile('Hello(.*)World') 
		>>> matchobj = pattobj.match(text1)
		>>> matchobj.group(1)
		'''
		
		'''
		HTMLSource = open ( iafd_search_results, 'r' )
		iafdHTML = BeautifulSoup ( HTMLSource )
		HTMLSource.close ( )
		'''
		
		results = open ( iafd_search_results, 'r' ).read ( )
		
		xxx_titles = re.findall('<li><b><a href=.*?>(.*?)</a></b>', results )
		

		
		found_a_name = False
		
		while not found_a_name :
		# get random selection
			potential_xxx_title = choice ( xxx_titles ) 
			potential_xxx_title_words = potential_xxx_title.split ( )
			
			# does the title have obvious give-away words?
			if not self.hasObviousWords ( potential_xxx_title_words ) :
				# does it have any numbers?
				if not re.match ( '.*\d.*', potential_xxx_title ) :
					found_a_name = True
	
		return potential_xxx_title

