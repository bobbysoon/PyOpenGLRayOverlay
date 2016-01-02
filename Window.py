from math import copysign,atan2

import sfml as sf

from OpenGL.GL import *
#from OpenGL.GLU import *
#from OpenGL.GL import shaders

import numpy

class Window:
	hasFocus=False
	window = sf.RenderWindow(sf.VideoMode(800, 600), "pySFML - OpenGL", sf.Style.DEFAULT, sf.ContextSettings(32))
	window.vertical_synchronization = True
	window.framerate_limit=15
	window.mouse_cursor_visible= False
	sf.Mouse.set_position(window.size/2, window)
	window.active = True
	size= window.size

	@staticmethod
	def getMousePos():
		return sf.Mouse.get_position(Window.window)

	@staticmethod
	def setMousePos(p):
		sf.Mouse.set_position(p, Window.window)

	@staticmethod
	def isOpen():
		for event in Window.window.events:
			if event == sf.CloseEvent: Window.window.close()
			if event == sf.ResizeEvent:
				Window.size= event.size
				glViewport(0, 0, event.width, event.height )
			if event == sf.FocusEvent:
				Window.hasFocus= event.gained # in theory, anyway
			if True or Window.hasFocus:
				if event == sf.KeyEvent and event.code == sf.Keyboard.ESCAPE:
					Window.window.close()

		return Window.window.is_open

	@staticmethod
	def display():
		Window.window.display()

	clock=sf.Clock()
	@staticmethod
	def Input(lookCurve=1.4):
		t=Window.clock.restart().seconds
		""" The actual camera setting cycle """
		wc= Window.size/2
		mouse_dx,mouse_dy = (Window.getMousePos()-wc)*t
		#mouse_dx= copysign(abs(mouse_dx)**lookCurve,mouse_dx)
		#mouse_dy= copysign(abs(mouse_dy)**lookCurve,mouse_dy)
		Window.setMousePos(wc)

		buffer = glGetDoublev(GL_MODELVIEW_MATRIX)
		c = (-1 * numpy.mat(buffer[:3,:3]) * numpy.mat(buffer[3,:3]).T).reshape(3,1)
		# c is camera center in absolute coordinates, 
		# we need to move it back to (0,0,0) 
		# before rotating the camera
		glTranslate(c[0],c[1],c[2])
		m = buffer.flatten()
		glRotate( -mouse_dx, m[1],m[5],m[9])
		glRotate( -mouse_dy, m[0],m[4],m[8])
		
		# compensate roll
		glRotated(-atan2(-m[4],m[5]) * 57.295779513082320876798154814105 ,m[2],m[6],m[10])
		glTranslate(-c[0],-c[1],-c[2])

		t*=10.0
		kb,k = sf.Keyboard.is_key_pressed,sf.Keyboard
		x= t if kb(k.A) else -t if kb(k.D) else .0
		z= t if kb(k.W) else -t if kb(k.S) else .0
		y= t if kb(k.L_SHIFT) else -t if kb(k.SPACE) else .0
		if z or x or y:
			#m = glGetDoublev(GL_MODELVIEW_MATRIX).flatten()
			glTranslate(z*m[2],z*m[6],z*m[10])
			glTranslate(x*m[0],x*m[4],x*m[8])
			glTranslate(y*m[1],y*m[5],y*m[9])

