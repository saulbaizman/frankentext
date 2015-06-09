#!/usr/bin/python
"""
Franktext. Generate an answer for the game using NLP and other tools. 
"""

from random import choice # to choose a random item from a list
import nltk
from config import debug


# import nltk stuff
# import mod1, mod2, ...

'''

NOTE: the NLTK corpora needs to be installed in a location suitable for the web server for this to work:

 Resource 'corpora/brown' not found.  Please use the NLTK
  Downloader to obtain the resource:  >>> nltk.download()
  Searched in:
    - '/Library/WebServer/nltk_data'
    - '/usr/share/nltk_data'
    - '/usr/local/share/nltk_data'
    - '/usr/lib/nltk_data'
    - '/usr/local/lib/nltk_data'

'''


'''
simplified tags:

>>> nltk.corpus.brown.tagged_words(simplify_tags=True)


>>> len (brown.words())
1161192

http://www.nltk.org/book/ch05.html

ADJ	adjective	new, good, high, special, big, local
ADV	adverb	really, already, still, early, now
CNJ	conjunction	and, or, but, if, while, although
DET	determiner	the, a, some, most, every, no
EX	existential	there, there's
FW	foreign word	dolce, ersatz, esprit, quo, maitre
MOD	modal verb	will, can, would, may, must, should
N	noun	year, home, costs, time, education
NP	proper noun	Alison, Africa, April, Washington
NUM	number	twenty-four, fourth, 1991, 14:24
PRO	pronoun	he, their, her, its, my, I, us
P	preposition	on, of, at, with, by, into, under
TO	the word to	to
UH	interjection	ah, bang, ha, whee, hmpf, oops
V	verb	is, has, get, do, make, see, run
VD	past tense	said, took, told, made, asked
VG	present participle	making, going, playing, working
VN	past participle	given, taken, begun, sung
WH	wh determiner	who, which, when, what, where, how

'''

'''
# choose 500 random words...
>>> tagged2 = nltk.corpus.brown.tagged_words(simplify_tags=True)[:500] # get a range
>>> just_nouns = [word for ( word, pos ) in tagged2 if pos == 'N' ]

>>> numbers = range ( len ( just_nouns2 )
>>> word1_index = choice ( numbers )
>>> word2_index = choice ( numbers )
>>> just_nouns[word1_index-1:word1_index]
>>> just_nouns[word2_index-1:word2_index]


>>> sentence = ''
>>> tagged_sent = pos_tag(sentence.split())

'''


class frankenText ( object ) :
	def __init__ (self):
		True

	def getName ( self ) :
	
		#return 'dummy text' 
	
		brown_corpus_length = 1161192
		
		indices = range ( brown_corpus_length-500 )
		
		random_index_start = choice (indices)
		
		tagged_words = nltk.corpus.brown.tagged_words(simplify_tags=True)[random_index_start:random_index_start+500]
		
		nouns = [word for ( word, pos ) in tagged_words if pos == 'N' ]
		adjectives = [word for ( word, pos ) in tagged_words if pos == 'ADJ' ]
		verbs = [word for ( word, pos ) in tagged_words if pos == 'V' ]

		templates = range ( 6 )
		
		template = choice ( templates )

		'''

		templates:

		[Noun] of the [Noun]
		
		[Noun] of [Noun]

		[Noun] the [Noun]

		[Noun] the [Adj]

		[Noun] [Noun]

		[Adj] [Noun]
		
		[Verb] the [Noun]

		'''

		if template == 0 :
			phrase = choice ( nouns ).title() + ' of the ' + choice ( nouns ).title()
			
		elif template == 1 :
			phrase = choice ( nouns ).title() + ' of ' + choice ( nouns ).title()

		elif template == 2 :
			phrase = choice ( nouns ).title() + ' the ' + choice ( nouns ).title()

		elif template == 3 :
			phrase = choice ( nouns ).title() + ' the ' + choice ( adjectives ).title()

		elif template == 4 :
			phrase = choice ( nouns ).title() + ' ' + choice ( nouns ).title()

		elif template == 5 :
			phrase = choice ( adjectives ).title() + ' ' + choice ( nouns ).title()

		else:
			phrase = choice ( verbs ).title() + ' the ' + choice ( nouns ).title()

		return phrase
