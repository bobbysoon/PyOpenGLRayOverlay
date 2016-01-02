from OpenGL.GL import *
from OpenGL.GLU import *

from Sphere import *

class Shader_Spheres:
	vert= open('Shader_Spheres.vert').read()
	frag= open('Shader_Spheres.frag').read()

	VERTEX_SHADER = shaders.compileShader(vert, GL_VERTEX_SHADER)
	FRAGMENT_SHADER = shaders.compileShader(frag, GL_FRAGMENT_SHADER)
	shadyMcShader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)

	shaderColor= glGetUniformLocation( shadyMcShader, 'color' )
	shaderMatrix= glGetUniformLocation( shadyMcShader, 'matrix' )

	@staticmethod
	def setColor(r,g,b,a):
		glUniform4f(Shader_Spheres.shaderColor, r,g,b,a)

	@staticmethod
	def setMatrix(r,g,b,a):
		modelview= glGetDoublev(GL_MODELVIEW_MATRIX)
		projection= glGetDoublev(GL_PROJECTION_MATRIX)
		viewport= glGetIntegerv(GL_VIEWPORT)

		glUniformMatrix4fv(Shader_Spheres.shaderMatrix, 1, GL_FALSE, modelview)

	@staticmethod
	def draw():
		shaders.glUseProgram(Shader_Spheres.shadyMcShader)
		Shader_Spheres.setColor(1,0,0,1);sphere1.draw()
		Shader_Spheres.setColor(0,0,1,1);sphere2.draw()

