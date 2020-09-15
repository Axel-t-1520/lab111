#Ingrese un tiempo X que estara representado en segundos,luego ingrese 
#el tiempo que tomara realizar una tarea Z representados en segundos ,
# minutos y horas se pide verificar si con el tiempo X se puede finalizar la tarea. 

print('ingrese segundos' )
r=int(input())
print('ingrese el tiempo de la tarea:')
h=int(input('hora:'))
m=int(input('minutos:'))
s=int(input('segundo:'))
x=(r//3600 and r//60)
if(x<h and x<m and x<s):
    print('se puede finalizar la tarea') 
else:
    (x>h and x>m and x>s)
    print('no se puede realizar la tarea')  
     


#utilizando el coefciente (a,b,c) de una ecuacion de segundo grado 
#se pide mostrar la naturaleza de sus raices

print('calcular una ecuacion cuadratica')
a=int(input('ingrese el valor de a: '))
b=int(input('ingrese el valor de b:'))
c=int(input('ingrese el valor de c:'))
if(a!=0):
        x1=(-b+(((b**2)-(4*c*a))**0.5))/(2*a)
        x2=(-b-(((b**2)-(4*c*a))**0.5))/(2*a)
        print('x1:',x1,'x2 :',x2)
else:
        print('a no puede ser cero')



#dado 3 valores (horas,minutos y segundos) se pide sumar un segundo

h=15
m=25
s=59
a=int(input('ingrese los segundos:'))
s=s+a
if(s>59):
    p=s//60
    s=s%60
    m=m+p
    if(m>59):
        r=m//60
        m=m%60
        h=h+p
        if(h>23):
                q=h//24
                h=h%24
      
print(format(h,'02'),':',format(m, '02'),':',format(s,'02'))

