#!/usr/bin/python
"""
Grab the name of a racehorse.
"""

import string
import urllib
from random import choice # to choose a random item from a list
from bs4 import BeautifulSoup
import re
from config import debug


class raceHorse ( object ) :

	def __init__ (self) :

		True

	def getName ( self ) :
		
		url_base = 'http://www.horses-and-horse-information.com/horsenames/' 
		
		alpha = list ( string.ascii_lowercase ) 
		
		letter = choice ( alpha ) 

		#letter= 'b'
		
		url = url_base + letter + '.shtml'
		#print '<!--',url,'-->'
		
		#print 'url',url
		
		socket = urllib.urlopen ( url )
		
		HTMLSource = socket.read ( )
		
		socket.close ( )
		
		raceHorseHTML = BeautifulSoup ( HTMLSource, "lxml" )
		
		names = raceHorseHTML.find_all('td',class_='text11black',text=re.compile(letter + "*"))
		
		random_name = choice ( names )
		
		# FIXME: make sure this returns something!
		return random_name.text
		


