#!/usr/bin/python
# encoding: utf-8
import sys

def escribe(s):
	print s

def suma(x,y):
	print "Haciendo suma..."
	sum= x+y
	return sum

def resta(x,y):
	print "Haciendo resta..."
	sum= y-x
	return sum

def main():
	numer= sys.argv[2]	
	numero= sys.argv[1]
	sumados= suma(int(numer),int(numero))
	restados= resta(int(numer),int(numero))
	escribe('Has introducido '+numero+' y '+numer+' en la entrada')
	escribe('Y la suma de ambos es '+str(sumados))
	escribe('Y la resta del primero menos el segundo es '+str(restados))

if (len(sys.argv)<2):
	print "Error: falta argumento"
	sys.exit(-1)
else:
	main()
