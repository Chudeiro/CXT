#!/usr/bin/python
# encoding: utf-8
# Programa que lee dos numeros introducidos, los suma, los resta y los multiplica
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

def mult(x,y):
	print "Haciendo multiplicion..."
	mul=x*y
	return mul

def main():
	numer= sys.argv[2]	
	numero= sys.argv[1]
	sumados= suma(int(numer),int(numero))
	restados= resta(int(numer),int(numero))
	multi= mult(int(numer),int(numero))
	escribe('Has introducido '+numero+' y '+numer+' en la entrada')
	escribe('Y la suma de ambos es '+str(sumados))
	escribe('Y la resta del primero menos el segundo es '+str(restados))
	escribe('La multiplicacion  de ambos es '+str(multi))
	escribe('La diferencia entre la sema y la resta es '+str(resta(restados,sumados)))
	escribe('Hecho por S.Luaces ')
	escribe('La fecha de la creacion es el 30 de mayo de 2014')
	print "Y fue un trabajo muy duro"
	escribe('La nueva modificacion se hizo el 2 de junio de 2014')
	print "Nos despedidmos, Adios!"

if (len(sys.argv)<2):
	print "Error: falta argumento"
	sys.exit(-1)
else:
	main()
