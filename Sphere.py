from OpenGL.GL import *
from OpenGL.GLU import *

class Sphere:
	quadratic = gluNewQuadric()
	gluQuadricNormals(quadratic, GLU_SMOOTH)
	gluQuadricTexture(quadratic, GL_TRUE)

	def __init__(self, pos, radius=1.0):
		self.pos=pos;self.radius=radius

	def draw(self):
		glPushMatrix()
		#glLoadIdentity()
		glTranslatef(*self.pos)
		gluSphere(Sphere.quadratic,self.radius,12,12)
		glPopMatrix()

c1= 1,2,3
c2= -1,-2,-3
sphere1= Sphere(c1)
sphere2= Sphere(c2)

Sphere.ca=c1,c2
