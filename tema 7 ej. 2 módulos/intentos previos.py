'''En este segundo ejercicios tendréis que crear un script que nos diga si es
la hora de ir a casa. Tendréis que hacer uso del modulo time.
Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
haréis una operación para calcular el tiempo que queda de trabajo.'''

# tema 7 ej nº2
import time

ver = time.time()
print(time.ctime())
print(ver)

tuple_time=time.localtime() #hora local 
print(time.strftime('%T',tuple_time))

print(time.localtime())
print('//////'*8)
info = time.localtime() #variable info tm significa --tuple time
print(info)
'''print(info.tm_year)
print(info.tm_mon)
print(info.tm_hour)'''

print('++++++'*8)

if info.tm_hour < 10:
    print('siga siga')
else:
    print('a la c a s a')

print('//////'*8)

if info.tm_hour  < 19:
    a = 19 - info.tm_hour 
    b = 60 - info.tm_min
    print('faltan:',a, 'Horas y ',b, 'minutos')# la logica sirve al parecer falta imprimir mejorando el formato convertirlo a str...
    print('')
    print('siga siga')
else:
    print('a la c a s a')

print('//////'*8)    

print(time.strftime('%T',tuple_time))



from datetime import datetime, timedelta, date, time

now_hour = datetime.now()
delta = timedelta(hours=2)
print(now_hour - delta)
print(now_hour + delta)    

print('//////'*8)

formato = "%X" 
ahora = datetime.now()
ahoraF = ahora.strftime(formato) 
aCasa = datetime(2022,1,1,19,00,00) 
aCasaF = aCasa.strftime (formato) # le doy el formato al date time que ingrese manual y lo paso a str
aCasaD = aCasa.strptime(aCasaF,formato) # parseo la str a dato para poder operar

print('ahoraF',ahoraF)
print(aCasa,"<------")
print('aCasaF',aCasaF)
print('aCasaD',aCasaD)

resul2 =  ahora - aCasaD # al parsear cambia el año a 1900 no lo pude resolver aun
resulF = resul2
print('resul2',resul2)


'''if resul2 >lim:
   
   # print('faltan:',a, 'Horas y ',b, 'minutos')# la logica sirve al parecer falta imprimir mejorando el formato convertirlo a str...
    print('')
    print('siga siga')
else:
    print('XXXXc a s a')

print('//////'*8)'''
