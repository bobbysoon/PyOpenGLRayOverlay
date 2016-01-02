from OpenGL.GL import *
#from OpenGL.GLU import *
import numpy

def UnProject(winx, winy, winz, modelMatrix=None, projMatrix=None, viewport=None):
	if None == modelMatrix: modelMatrix= glGetDoublev(GL_MODELVIEW_MATRIX)
	if None == projMatrix: projMatrix= glGetDoublev(GL_PROJECTION_MATRIX)
	if None == viewport: viewport= glGetIntegerv(GL_VIEWPORT)

	npModelMatrix = numpy.matrix(numpy.array(modelMatrix, numpy.float64).reshape((4,4)))
	npProjMatrix = numpy.matrix(numpy.array(projMatrix, numpy.float64).reshape((4,4)))
	finalMatrix = npModelMatrix * npProjMatrix
	finalMatrix = numpy.linalg.inv(finalMatrix)

	viewport = map(float, viewport)
	vector = numpy.array([(winx - viewport[0]) / viewport[2] * 2.0 - 1.0, (winy - viewport[1]) / viewport[3] * 2.0 - 1.0, winz * 2.0 - 1.0, 1]).reshape((1,4))
	vector = (numpy.matrix(vector) * finalMatrix).getA().flatten()
	vec3 = list(vector)[0:3] / vector[3]
	return (vec3).tolist()

