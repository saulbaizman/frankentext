#!/usr/bin/python

"""
frankentext, an HTML-based quiz game.
"""

'''
What is the flow?

If someone gets the answer wrong, do they get another shot at it? Are they told which one was the correct answer?

--

The time should be reduced for every new level (30, 20, 10), and the entries should be more ambiguous.

--

Next level automatic pop-up to announce the level, point change, and time difference?

--

Add another sound effect for making it to the high score

TO DO
+ adding name to high score list.
#+ losing all of your lives.
#+ making it to the end of the game.
+ Update the rock band sound to be a guitar strum 
+ Add animation per Brian's suggestion
'''



'''
TO DO

+ Add high scores listing and data entry. (half-done)

#+ 'Next' button should only light up after an answer has been selected.

#+ Keep a history of recent names, so it doesn't repeat.

+ Add link to start over

#+ Fix up intro page
#	+ Add credits

Some architecture questions: should the system load up on names at the beginning, rather than loading them on every pageload? Everything will go faster if the program does this.

'''

'''
For NLTK, download the corpora:

>>> import nltk
>>> nltk.download()
then, move the nltk_data folder elsewhere
'''


'''
ALTERNATE

Showing two different names, one from a person, one from a computer, and rating which name is better or who is a better writer.

'''

'''
ISSUE: when a name is in multiple caltegories!
To do: make a lookup to exclude the existince from other categories.
'''

# learn how to use shelves; store high scores in it
# is there a switch statement in Python?

# from bs4 import BeautifulSoup
#import urllib
from random import choice # to choose a random item from a list
import cgi
import cgitb # for debugging
cgitb.enable() # or, to log to a file: cgitb.enable(display=0, logdir="/path/to/logdir")

import shelve

'''
VERY OLD NOTES BELOW
--------------------
The level and question number can be set and identified via the query string. Example: 

  http://frankentext/franketext.py?level=1&q=5

The score of the user can be kept in a file / shelve. that's packed and unpacked when the page is loaded.   


Q: how does the system know / store which answer is correct?


Note: need next button? or next advance? [after a question has been answered]

When the system hasn't been touched in a while and needs to be reset to its default, it should forward the browser to http://noneoftheabove/none.py?reset=1, which goes to the homepage / instruction page and wipes out the score of the previous player.

Architecture note: the webpages should be external "templates" whose values are substituted. This will keep HTML out of the python script.


'''

'''
To poulate the leader board, I went into the python IDLE and issued the following commands:

db = shelve.open ( 'leader-board')
db['A'] = { 'player' : 'MJB', 'rank' : 1, 'score' : 1600 }
db['B'] = { 'player' : 'AJB', 'rank' : 2, 'score' : 1200 }
db['C'] = { 'player' : 'SRB', 'rank' : 3, 'score' : 1000 }
db.close()

Be sure the permissions on the 'leader-board' file allow the web server user to read and write to this file!

FIXME: also include the level and question no.?

'''

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

# FUNCTIONS
# note: they need to be defined before they're invoked!

def print_comment ( variable_name, variable_value ):
	print "<!--",variable_name,":", variable_value, "-->" 

# for debugging purposes; prints out all of an object's attributes
def print_attributes ( obj ) :
	for attr in obj.__dict__ :
		print attr, getattr(obj, attr)

def getName ( this_question_type ) :
	if  this_question_type == 'frankenText':
		newNameObject = frankenText.frankenText ( )

	elif this_question_type == 'raceHorse' :
		newNameObject = raceHorse.raceHorse ( )
		
	elif this_question_type == 'rockBand' :
		newNameObject = rockBand.rockBand ( )
	
	elif this_question_type == 'porno' :
		newNameObject = xxxFilm.xxxFilm ( )

	else :
		# how did we get here?
		# quit the loop
		print 'invalid question type'

	return newNameObject

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################

# GLOBAL VARIABLES from config.py
from config import debug
from config import template_directory
from config import program_name
from config import leader_board_db # leader board!
from config import recent_names_db # this empty db must exist before the game is run
from config import score_keeper_db # keeps track of the user's score and lives
#import unknownName

answer_types = [ 'frankenText', 'raceHorse', 'rockBand', 'porno' ] ;
#answer_types = [ 'raceHorse' ] ;
#answer_types = [ 'frankenText' ] ;
#answer_types = [ 'porno' ] ;
#answer_types = [ 'frankenText', 'raceHorse', 'rockBand' ] ;

# map(__import__, answer_types)

'''
for answer_type in answer_types:
	import answer_type 
'''
import frankenText
import raceHorse
import rockBand
import xxxFilm

# template definitions
instruction_template = template_directory + '/' + 'instructions.html'
question_template = template_directory + '/' + 'question.html'

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################


# grab the URL query string data
script_arguments = cgi.FieldStorage ()
# these are the only legal parameters in the query string
parameters = ( 'question' , 'level' )

# if neither parameter is in the script_arguments, default to the instruction page.


# basic primer for CGI:
# https://wiki.python.org/moin/CgiScripts

print "Content-type: text/html"
print #don't forget this necessary blank line, or you'll get nasty "malformed header from script. Bad header=<head>:" messages in the apache error log

'''
We also need to keep track of two post variables:
 - the answer the user has chosen.
 - the hidden field that contains the correct answer.

We'll need to see if they are present as well.
'''

# Page 24: shelves.

# open db of recently used names
recent_names = shelve.open ( recent_names_db )
# open score
score_keeper = shelve.open ( score_keeper_db )


if not ( 'question' or 'level' ) in script_arguments:
	instructions = open ( instruction_template, 'r' )
	instructions_html = instructions.read ( )
	instructions_html = instructions_html.replace ( '$PROGRAM_NAME$' , program_name )
	
	# open the shelve, grab the top scorers
	top_scores = shelve.open ( leader_board_db )
	
	# how are the ranks to be determined? what if there's a tie?
	# the ranks are saved in the DB. they will have to be computed prior to saving them.
	
	player_1 = top_scores['A']['player']
	player_1_score = str ( top_scores['A']['score'] )
	player_2 = top_scores['B']['player']
	player_2_score = str ( top_scores['B']['score'] )
	player_3 = top_scores['C']['player']
	player_3_score = str ( top_scores['C']['score'] )
	
	top_scores.close ( )
	
	# populate the top scores	
	instructions_html = instructions_html.replace ( '$PLAYER_1$' , player_1 )
	instructions_html = instructions_html.replace ( '$PLAYER_1_SCORE$' , player_1_score )
	instructions_html = instructions_html.replace ( '$PLAYER_2$' , player_2 )
	instructions_html = instructions_html.replace ( '$PLAYER_2_SCORE$' , player_2_score )
	instructions_html = instructions_html.replace ( '$PLAYER_3$' , player_3 )
	instructions_html = instructions_html.replace ( '$PLAYER_3_SCORE$' , player_3_score )

	
	print instructions_html
	# see page 1195 in Programming Python for adding variables in the template and replacing them in the print statement.
	instructions.close ( ) 
	
	# close/clear out the shelve, if needed
	if len ( recent_names ) > 0 :
		for name in recent_names :
			del ( recent_names[name] )
		recent_names.close ( )

else:
	
	# are we on a valid level?
	if script_arguments.getvalue ( 'level' ) == '0' :
		is_valid_level = True
		score_increment = 100
	elif script_arguments.getvalue ( 'level' ) == '1' :
		is_valid_level = True 
		score_increment = 200
	elif script_arguments.getvalue ( 'level' ) == '2' :
		is_valid_level = True 
		score_increment = 300
	else:
		# error message
		is_valid_level = False 
		print "invalid level."

	# if we're on the first question of the first level, reset the score and player lives
	if script_arguments.getvalue ( 'level' ) == '0' and script_arguments.getvalue ( 'question' ) == '0' :
		score_keeper['score'] = 0 
		score_keeper['lives'] = 3 

	# is the question a number, less than 0, or greater than 10?
	
	# a check for number (http://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not):
	# isinstance ( script_arguments.getvalue('question'), ( int, long ) )
	
	# note that the query string arguments are strings, and we have to cast them 
	# as integers (http://stackoverflow.com/questions/3979077/how-can-i-convert-a-string-to-an-int-in-python) 
	#print type ( script_arguments.getvalue('question') ) 

	# are we on a valid question number?
	if int ( script_arguments.getvalue ( 'question' ) ) < 0 or int ( script_arguments.getvalue ( 'question' ) )  > 10 :
		is_valid_question = False
	else:
		is_valid_question = True


	# if the question and level check out...		
	if is_valid_question and is_valid_level:
	
		
		# Search for a name that we haven't used already.
		found_a_name = False
		
		while not found_a_name :
		# get random selection
			this_question_type = choice ( answer_types ) 
			newNameObject = getName ( this_question_type )
			unknown_name = newNameObject.getName ( )
			if unknown_name not in recent_names_db : # not a case-insensitive search!
				found_a_name = True

		# add the name to the recent names list, then close shelve
		# TODO: store whether the user's answer was correct!
		recent_names[str(unknown_name)] = this_question_type
		recent_names.close ( )
		
		# subtract lost lives
		if 'remove_life' in script_arguments:
			if score_keeper['lives'] > 0 :
				score_keeper['lives'] -= 1

		# add points to score
		if 'increment_score' in script_arguments:
			score_keeper['score'] += int ( script_arguments.getvalue ( 'increment_score' ) )

		# if we're on question 1, level 1,
		# open the shelve to populate the data, if it's a brand-new game

		# if we're NOT on question 1, level 1,
		# open the shelve to get the old data

		# see page 1195 in PP for adding variables in the template and replacing them in the print statement.
		
		# pretty-print the indefinite article, or not
		if this_question_type == 'frankenText' :
			article = ''
		else : 
			article = 'a '
		
		extra_bit = ''		
		# set the level based on the question number
		# *****must end at third level!*****
		if int ( script_arguments.getvalue ( 'question' ) ) == 9 :
			# question or level
			phase = 'level'
			next_level = int ( script_arguments.getvalue ( 'level' ) ) + 1
			if next_level == 1 :
				extra_bit = '<p class="next_level_note"><strong>Note</strong>: you only have <big><u>20 seconds</u></big> to respond, and each correct answer is worth <big><u>200 points</u></big>.</p>'
			elif next_level == 2 :
				extra_bit = '<p class="next_level_note"><strong>Note</strong>: you only have <big><u>10 seconds</u></big> to respond, and each correct answer is worth <big>300 points</big>.</p>'
		else : 
			# question or level
			phase = 'question'
			next_level = int ( script_arguments.getvalue ( 'level' ) )
		
		# set the question number
		if int ( script_arguments.getvalue ( 'question' ) ) == 9 :
			next_question = 0
		else :
			next_question = int ( script_arguments.getvalue ( 'question' ) ) + 1 
		
		# set the score increment based on the level ( 1 => 100, 2 => 200, 3 => 300 )
		'''		
		if next_level is 0 :
			score_increment = 100
		elif next_level is 1 :
			score_increment = 100
		elif next_level is 2 :
			score_increment = 100
		else:
			score_increment = 0
			# houston, we have a problem
		'''
		
		#lives_html = str ( score_keeper['lives'] )
		f_head = '<img src="tmpl/image/f-head.png"> '
		f_head_dead = '<img src="tmpl/image/f-head-dead.png"> '
		lives_html = (f_head*score_keeper['lives'])+(f_head_dead*(3-score_keeper['lives']))
		
		question = open ( question_template, 'r' )
		question_html = question.read ( )
		question_html = question_html.replace ( '$PROGRAM_NAME$' , program_name )
		question_html = question_html.replace ( '$LIVES$' , str ( score_keeper['lives'] ) )
		question_html = question_html.replace ( '$LIVES_HTML$' , lives_html )
		level_number = int ( script_arguments.getvalue ( 'level' ) ) + 1
		question_html = question_html.replace ( '$LEVEL$' ,  str ( level_number ) )
		question_html = question_html.replace ( '$SCORE$' , str ( score_keeper['score'] ) )
		question_number = int ( script_arguments.getvalue ( 'question' ) ) + 1
		question_html = question_html.replace ( '$QUESTION$' ,  str ( question_number ) )
		question_html = question_html.replace ( '$UNKNOWN_NAME$' , unknown_name )
		question_html = question_html.replace ( '$QUESTION_TYPE$' , this_question_type )
		question_html = question_html.replace ( '$CORRECT_ANSWER$' , this_question_type )
		question_html = question_html.replace ( '$ARTICLE$' , article )
		question_html = question_html.replace ( '$PHASE$' , phase )
		question_html = question_html.replace ( '$EXTRA$' , extra_bit )
		question_html = question_html.replace ( '$NEXT_QUESTION$' , str ( next_question ) )
		question_html = question_html.replace ( '$NEXT_LEVEL$' , str ( next_level ) )
		question_html = question_html.replace ( '$SCORE_INCREMENT$' , str ( score_increment ) )
		
		# print question_html % ( program_name, int ( script_arguments.getvalue ( 'level' ) ) +1, int ( script_arguments.getvalue ( 'question' ) ) +1, unknown_name, this_question_type ) 
		
		print question_html 
				
		score_keeper.close ( )
		question.close ( ) 
	else:
		# error message
		print 'invalid question or level'


'''
	print """
	<html><head>
	<title>Frankentext</title>
	</head><body>
	spit out a template
	"""
'''

	# FIXME: print out all script arguments.
if debug:
	#print_comment ( 'this question type', this_question_type ) 
	print_comment ( 'debug', debug ) 
	print_comment ( 'script arguments', script_arguments ) 
	print_comment ( 'instruction template', instruction_template ) 
	print_comment ( 'question', script_arguments.getvalue('question') ) 
	print_comment ( 'level', script_arguments.getvalue('level') ) 
		
'''	
	print """
	</body></html>
	"""	
'''
