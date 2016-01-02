#!/usr/bin/python

from __future__ import division

from Window import *
from initOpenGL import * # glMatrixMode(GL_MODELVIEW)
from Shader_Spheres import *
from Shader_Render import *


while Window.isOpen():
	if Window.hasFocus:
		Window.Input()

		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		Shader_Spheres.draw() # drawn using gluSphere
		Shader_Render.draw() # 'glow' is 1.0/(sphere point's distance from pixel's ray)
		Window.display()



