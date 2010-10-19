from pyglet import window
from pyglet import font
from pyglet.window import key
from pyglet.gl import *

win = window.Window()
win.set_fullscreen(True)

class Engine:
	"The starts of an engine class"

	ft = font.load( None, win.height * .8 )

	letter = 'B'

	letter_x = win.width / 2
	letter_y = win.height / 2

	red = 1;
	blue = 1;
	green = 1;
	alpha = 1;

	backred = 0.0;
	backblue = 0.0;
	backgreen = 0.0;
	backalpha = 1.0;

	text = font.Text(ft, letter );

	def set_back(self):
		glClearColor( self.backred, self.backblue, self.backgreen, self.backalpha )
		glClear(GL_COLOR_BUFFER_BIT)

	def set_text(self):
		self.text = font.Text( self.ft, 
			self.letter,
			x = self.letter_x,
			y = self.letter_y,
			halign = font.Text.CENTER,
			valign = font.Text.CENTER)
		self.text.color = ( 
			self.red, 
			self.green, 
			self.blue, 
			self.alpha ) 

	def update(self):
		self.set_back()
		self.set_text()

eng = Engine();

def get_multiplier( keylist, keyindex ):
	multiplier_list = [ .75, .8, .85, .9, .95, 1, 1.05, 1.1, 1.15, 1.2, 1.25 ]

	distance = keyindex - ( len(keylist) / 2 )
	multiplier_center = len( multiplier_list ) / 2
	return multiplier_list[ multiplier_center + distance ]
		
def on_key_press( symbol, modifiers ):
	top_row = [key.Q, key.W, key.E, key.R, key.T, key.Y, key.U, key.I, key.O, key.P ]
	mid_row = [key.A, key.S, key.D, key.F, key.G, key.H, key.J, key.K, key. L ]
	bot_row = [key.Z, key.X, key.C, key.V, key.B, key.N, key.M ]
	
	keylist = False
	if symbol in top_row:
		eng.red *= get_multiplier( top_row, top_row.index( symbol ) )
	elif symbol in mid_row:
		eng.green *= get_multiplier( mid_row, mid_row.index( symbol ) )
	elif symbol in bot_row:
		eng.blue *= get_multiplier( bot_row, bot_row.index( symbol ) )

	if eng.red < 0:
		eng.red = 0.01
	if eng.red > 1:
		eng.red = 1
	if eng.green < 0:
		eng.green = 0.01
	if eng.green > 1:
		eng.green = 1
	if eng.blue < 0:
		eng.blue = 0.01
	if eng.blue > 1:
		eng.blue = 1
		
	eng.backred = 1.0 - eng.red
	eng.backblue = 1.0 - eng.blue
	eng.backgreen = 1.0 - eng.green	
		
def on_text( text ):
	eng.letter = text
	eng.update()

win.push_handlers( on_key_press, on_text )

while not win.has_exit:
	win.dispatch_events()

	win.clear()
	eng.text.draw()
	win.flip()
