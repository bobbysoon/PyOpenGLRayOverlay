from OpenGL.GL import *
from OpenGL.GLU import *

from Sphere import *

from UnProject import UnProject

class Shader_Render:
	vert= open('Shader_Render.vert').read()
	frag= open('Shader_Render.frag').read()

	VERTEX_SHADER = shaders.compileShader(vert, GL_VERTEX_SHADER)
	FRAGMENT_SHADER = shaders.compileShader(frag, GL_FRAGMENT_SHADER)
	shadyMcShader = shaders.compileProgram(VERTEX_SHADER,FRAGMENT_SHADER)

	res=		glGetUniformLocation( shadyMcShader, 'res' )

	c1=			glGetUniformLocation( shadyMcShader, 'c1' )
	c2=			glGetUniformLocation( shadyMcShader, 'c2' )

	near11=			glGetUniformLocation( shadyMcShader, 'near11' )
	near12=			glGetUniformLocation( shadyMcShader, 'near12' )
	near21=			glGetUniformLocation( shadyMcShader, 'near21' )
	near22=			glGetUniformLocation( shadyMcShader, 'near22' )
	far11=			glGetUniformLocation( shadyMcShader, 'far11' )
	far12=			glGetUniformLocation( shadyMcShader, 'far12' )
	far21=			glGetUniformLocation( shadyMcShader, 'far21' )
	far22=			glGetUniformLocation( shadyMcShader, 'far22' )

	@staticmethod
	def draw(m=0):
		shaders.glUseProgram(Shader_Render.shadyMcShader)

		if m:
			glMatrixMode(GL_MODELVIEW);glPushMatrix();glLoadIdentity()
			glMatrixMode(GL_PROJECTION);glPushMatrix();glLoadIdentity()

		v=	glGetFloatv(GL_VIEWPORT)
		glUniform2f(Shader_Render.res, v[2],v[3])

		c1,c2=Sphere.ca
		glUniform3f(Shader_Render.c1, *c1)
		glUniform3f(Shader_Render.c2, *c2)

		Shader_Render.unPro()

		glRectf(-.75,-.75,.75,.75)
		#glRectf(-1,-1,1,1)

		if m:
			glPopMatrix();glMatrixMode(GL_MODELVIEW);glPopMatrix()

	@staticmethod
	def unPro():
		viewport = glGetIntegerv( GL_VIEWPORT )
		modelMatrix = glGetDoublev( GL_MODELVIEW_MATRIX )
		projMatrix = glGetDoublev( GL_PROJECTION_MATRIX )
		w,h=viewport[2:]

		glUniform3f(Shader_Render.near11, *UnProject(0,0,0, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))
		glUniform3f(Shader_Render.near12, *UnProject(0,h,0, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))
		glUniform3f(Shader_Render.near21, *UnProject(w,0,0, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))
		glUniform3f(Shader_Render.near22, *UnProject(w,h,0, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))

		glUniform3f(Shader_Render.far11, *UnProject(0,0,-1, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))
		glUniform3f(Shader_Render.far12, *UnProject(0,h,-1, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))
		glUniform3f(Shader_Render.far21, *UnProject(w,0,-1, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))
		glUniform3f(Shader_Render.far22, *UnProject(w,h,-1, modelMatrix=modelMatrix, projMatrix=projMatrix, viewport=viewport))

