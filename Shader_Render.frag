#version 120

uniform vec3 near11;
uniform vec3 near12;
uniform vec3 near21;
uniform vec3 near22;
uniform vec3 far11;
uniform vec3 far12;
uniform vec3 far21;
uniform vec3 far22;

uniform vec2 res;

uniform vec3 c1;
uniform vec3 c2;
float cRadius=1.0;

float pointLineDist( vec3 P, vec3 lo, vec3 ld) {
	vec3 w = P - lo;
	
	float c1 = dot(w,ld);
	float c2 = dot(ld,ld);
	float b = c1 / c2;
	
	vec3 Pb = lo + b * ld;
	return length(P-Pb);
}

float pointRayDist( vec3 P, vec3 lo, vec3 ld) {
	vec3 w = P - lo;
	
	float c1 = dot(w,ld);
	float c2 = dot(ld,ld);
	float b = c1 / c2;
	float l = length(P-(lo + b * ld));
	return b<0 ? l : -l ; // ? idk. w/e
}

void main() {
	gl_FragColor.a=0.5;
	float x= gl_FragCoord.x/res.x , y= gl_FragCoord.y/res.y;
	vec3 l,r;
	l= near11+y*(near12-near11);
	r= near21+y*(near22-near21);
	vec3 p1= l+x*(r-l);
	l= far11+y*(far12-far11);
	r= far21+y*(far22-far21);
	vec3 p2= l+x*(r-l);

	vec3 d= normalize(p2-p1);

	float d1=pointRayDist( c1, p1,d);
	float d2=pointRayDist( c2, p1,d);

	gl_FragColor.r=1./d1;
	gl_FragColor.b=1./d2;
	gl_FragColor.g=.0;
	gl_FragColor.a=.5;
}



