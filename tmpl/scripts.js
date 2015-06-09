/*

FIXME: "time's up" and "wrong" messages on the very last question should lead to some congrats message.

FIXME: add stats to 'game over' message.

FIXME: finish programming adult movie data parsing!

FRANKENTEXT

*/

var debug = false ; // disables a bunch of annoying stuff when 'true'

var level = window.level ;
var question = window.question ;
var lives = window.lives ;

game_reset_timeout_count = 300 // 5 minutes of inactivity throws people back to the beginning screen.

timer_count = 31

if ( ! debug )
{
	// production values
	if ( level == 1 )
	{
		var count = timer_count ; // 30 seconds
	}
	else if ( level == '2' )
	{
		var count = timer_count-10 ; // 20 seconds
	}
	else if ( level == '3' )
	{
		var count = timer_count-20 ; // 10 seconds
	}	
	else
	{
	// houston, we have a problem
	}

}
else
{
	var count=11; // dev
}

// start the timers, if we're not viewing the instructions
if ( level == '1' || level == '2' || level == '3' )
{
	var counter=setInterval(startTimer, 1000); //1000 will run it every 1 second

	var counter2=setInterval(startGameResetTimer, 1000); //1000 will run it every 1 second
}

// jquery test
// $('a').click(function() { alert('hello'); });

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function unlockGo ( )
{
	// unlock the go / next button

	if ( document.getElementById('go').disabled )
	{
		document.getElementById('go').disabled = false ;
		document.getElementById('go').style.background = 'green' ;
		document.getElementById('go').style.border = 'green' ;
		document.getElementById('go').style.transition = 'background-color 0.5s ease' ;
		// transition:background-color 0.3s ease;
		// opacity?
		// document.getElementById('go').style.border = 'green' ;
	}

}

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function startGameResetTimer ( )
{
	if ( ! debug )
	{
		game_reset_timeout_count -= 1

		if (game_reset_timeout_count <= 0 )
		{
			window.location.assign("http://frankentext/game.py")
		}

	}
}


/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function startTimer ( )
{

	count = count-1 ;

	if ( count < 10 )
	{
		seconds = '0' + count ;
	}
	else
	{
		seconds = count ;
	}

	// note: the time should start making noise or look different
	document.getElementById("timer").innerHTML='0:' + seconds; 
	
	if (count <= 0 )
	{
		 clearInterval(counter);
		 
		 if ( ! debug )
		 {
		
			// if you have one life left, and it times out, the game's over!
			if ( lives == 1 ) 
			{
				var snd = new Audio ( ) ;
				snd.src = 'tmpl/sound/game-over.mp4' ;
				snd.addEventListener ( "canplaythrough", function () {
					snd.play ( ) ;
				}) ;
				snd.load ( ) ;

				$.fancybox( [$("#gameOverOutOfTime")],
				{
						closeClick  : false,
						openEffect  : 'none',
						closeEffect : 'none',		
						helpers   : { 
						overlay : {
						closeClick: false
						} // prevents closing when clicking OUTSIDE fancybox 
					  }
				});
			}
			// otherwise, you're just out of time.
			else
			{
				var snd = new Audio ( ) ;
				snd.src = 'tmpl/sound/time-is-up.mp4' ;
				snd.addEventListener ( "canplaythrough", function () {
					snd.play ( ) ;
				}) ;
				snd.load ( ) ;

				$.fancybox( [$("#youAreOutOfTime")],
				{
						closeClick  : false,
						openEffect  : 'none',
						closeEffect : 'none',		
						helpers   : { 
						overlay : {
						closeClick: false
						} // prevents closing when clicking OUTSIDE fancybox 
					  }
				});
		
			}
		}

	}

}

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function checkAnswer ( )
{
/*
http://stackoverflow.com/questions/15839169/how-to-get-value-of-selected-radio-button
*/
	
	// stop the timer
	clearInterval(counter);
	
	var correct_answer = $("input[name=correct_answer]").val() ;
	var user_answer = $("input[name=user_answer]:checked").val() ;
	
	// alert ( 'correct answer: ' +  $("input[name=correct_answer]").val() ) ;
	
	/*
http://stackoverflow.com/questions/8400433/jquery-fancybox-2-0-3-prevent-close-on-click-outside-of-fancybox	
	*/
	// CORRECT
	if ( user_answer == correct_answer )
	{
		// must come first
		if ( ! debug )
		{
			var snd = new Audio ( ) ;
			snd.src = 'tmpl/sound/three-dings-bell.mp4' ;
			snd.addEventListener ( "canplaythrough", function () {
				snd.play ( ) ;
			}) ;
			snd.load ( ) ;
		}
	
		// alert ( 'correct!' ) ;
		// trigger francybox
		
		if ( level == '3' && question == '10' )
		{
			// END OF THE GAME!
			$.fancybox( [$("#gameCompleted")],
			{
					closeClick  : false,
					openEffect  : 'none',
					closeEffect : 'none',		
					helpers   : { 
					overlay : {
					closeClick: false
					} // prevents closing when clicking OUTSIDE fancybox 
				  }
			});
		}
		else
		{
		
			$.fancybox( [$("#youAreCorrect")],
			{
					closeClick  : false,
					openEffect  : 'none',
					closeEffect : 'none',		
					helpers   : { 
					overlay : {
					closeClick: false
					} // prevents closing when clicking OUTSIDE fancybox 
				  }
			});
		}
	}
	else
	// WRONG
	{
		// alert ( 'WRONG!' ) ;

		// must come first

		// trigger francybox
		
		if ( lives == 1 ) 
		{
			if ( ! debug )
			{
				var snd = new Audio ( ) ;
				snd.src = 'tmpl/sound/game-over.mp4' ;
				snd.addEventListener ( "canplaythrough", function () {
					snd.play ( ) ;
				}) ;
				snd.load ( ) ;
			}		
/*

helpers : {
        overlay : {
            css : {
                'background' : 'rgba(58, 42, 45, 0.95)'
            }
        }
    }
*/
			$.fancybox( [$("#gameOver")],
			{
					closeClick  : false,
					openEffect  : 'none',
					closeEffect : 'none',		
					helpers   : { 
					overlay : {
					closeClick: false,
					css : { 'background' : 'rgba(0, 0, 0, 1)' }
					} // prevents closing when clicking OUTSIDE fancybox 
				  }
			});
		}
		else
		{
			if ( ! debug )
			{
				var snd = new Audio ( ) ;
				snd.src = 'tmpl/sound/buzzer.mp4' ;
				snd.addEventListener ( "canplaythrough", function () {
					snd.play ( ) ;
				}) ;
				snd.load ( ) ;
			}

			$.fancybox( [$("#youAreWrong")],
			{
					closeClick  : false,
					openEffect  : 'none',
					closeEffect : 'none',		
					helpers   : { 
					overlay : {
					closeClick: false
					} // prevents closing when clicking OUTSIDE fancybox 
				  }
			});
		}
	}
}

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function playSound ( sound )
{
	/*
	racehorse
	rockband
	adultfilm
	frankentext
	*/

	if ( ! debug )
	{
		var snd = new Audio ( ) ;

		if ( sound == 'racehorse' )
		{
				snd.src = 'tmpl/sound/horse-winnie.mp4' ;
		}
		else if ( sound == 'rockband' )
		{
				snd.src = 'tmpl/sound/rockband.mp4' ;
		}
		else if ( sound == 'adultfilm' )
		{
				snd.src = 'tmpl/sound/adult-film.mp4' ;
		}
		else if ( sound == 'frankentext' )
		{
				snd.src = 'tmpl/sound/franken-moan.mp4' ;
		}
		else
		{
			// houston, we have a problem 
		}

		snd.addEventListener ( "canplaythrough", function () {
			snd.play ( ) ;
		}) ;
		snd.load ( ) ;
		
	}
}

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function credits ( )
{
	$.fancybox( [$("#creditsInfo")] );
}

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function closeCredits ( )
{
	$.fancybox.close();

}

/*******************************************************************************
********************************************************************************
********************************************************************************
********************************************************************************
*******************************************************************************/

function goToPage ( page, div )
{
var opts = {
  lines: 15, // The number of lines to draw
  length: 20, // The length of each line
  width: 10, // The line thickness
  radius: 30, // The radius of the inner circle
  corners: 1, // Corner roundness (0..1)
  rotate: 0, // The rotation offset
  direction: 1, // 1: clockwise, -1: counterclockwise
  color: '#000', // #rgb or #rrggbb or array of colors
  speed: 1, // Rounds per second
  trail: 60, // Afterglow percentage
  shadow: false, // Whether to render a shadow
  hwaccel: false, // Whether to use hardware acceleration
  className: 'spinner', // The CSS class to assign to the spinner
  zIndex: 2e9, // The z-index (defaults to 2000000000)
  top: '200', // Top position relative to parent in px
  left: '500' // Left position relative to parent in px
};
	var target = document.getElementById(div);
	var spinner = new Spinner(opts).spin(target);	
	window.location.assign(page)
}
