# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 17:41:48 2019

@author: Familia
"""

#OBS: Estamos trabajando con SCRIPT, TEST Y SCORE dentro del mismo proyecto para que todo funcione


#Archivos que vamos a usar con funciones externas
import datetime 
import collections

# unordered set y las operaciones a usar
s = set([1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]) 
ops={"*","+","-","/"}

#Funcion que realiza  las operacion o entre dos números u y v
def op( u, v, o): 
    if o=="*":
        return u*v
    if o=="+":
        return u+v
    if o=="-":
        return u-v
    if o=="/" and u%v==0:
        return int(u/v)

#Busqueda en anchura desde desde dos puntos
#Empezamos desde los primos y el destino n y queremos llegar a un nexo que una los caminos
#dist, dist_inv,ch y ch_inv guardan, para cada entero por el que pasamos, el estado
#en el que se encuentran la cadena de numeros y operaciones, respectivamente
#Notese que dist_inv y ch_inv guardan el camino con las operciones y el orden inverso al que queremos

def bfs( n, p):
    dist={}; dist_inv={} 
    ch={}; ch_inv={}
    ss=s.copy()
    ss.remove(p)
    q = collections.deque(); q_inv = collections.deque() 
    for u in ss:
        dist[u]=[u]; ch[u]=[]
        if u==n:
            return [dist[u],ch[u],[],[]] 
        q.append(u)
    q_inv.append(n)
    dist_inv[n]=[]; ch_inv[n]=[]
    while len(q)!=0:
        u = q[0]; a = q_inv[0]
        while len(dist[u])<=len(dist_inv[a]):
            u = q[0]
            q.popleft()
            for v in ss:   
                for o in ops: 
                    w=op(u,v,o)
                    if w not in dist.keys() and w!=None and w>0: 
                        dist[w]= dist[u].copy()
                        dist[w].append(v)
                        ch[w] = ch[u].copy()
                        ch[w].append(o)
                        q.append(w)
                        if w in dist.keys() and w in dist_inv.keys():
                            return [dist[w],ch[w],dist_inv[w],ch_inv[w]]
        while len(dist[u])>len(dist_inv[a]):
            a = q_inv[0]
            q_inv.popleft()
            for v in ss:   
                for o in ops: 
                    y=op(a,v,o)
                    if y not in dist_inv.keys() and y!=None: 
                        dist_inv[y]= dist_inv[a].copy()
                        dist_inv[y].append(v)
                        ch_inv[y] = ch_inv[a].copy()
                        ch_inv[y].append(o)
                        q_inv.append(y)
                        if y in dist.keys() and y in dist_inv.keys():
                            return [dist[y],ch[y],dist_inv[y],ch_inv[y]]


#Función que toma el resultado de bfs y devuelve lo que necesitamos mostar
def display(num_1,ope_1,num_2,ope_2):
    long=len(num_1)+len(num_2)#Cantidad de números empleados
    result=str(num_1[0])#result el el primer numero sobre el que construimos la formula
    num_1.pop(0)#quitamos el primer número de la lista para tener las mismos numeros que operaciones
    lista_1=zip(num_1,ope_1)#juntamos en una lista de dos elementos los numeros y operaciones del camino desde los primos
    for elem in lista_1:#A cada elemento de la union lo vamos añadiendo sobre lo anterior
        result= '(' + result + str(elem[1]) + str(elem[0]) + ')'#Pone la operacion y el numero nuevos
    change=[]#lista para luego
    num_2.reverse(); ope_2.reverse()#Damos la vuelta a los caminos desde n
    for ope in ope_2:# Y también invertimos las operaciones
        if ope=="+":
            change.append("-")
        if ope=="-":
            change.append("+")
        if ope=="*":
            change.append("/")
        if ope=="/":
            change.append("*")
    lista_2=zip(num_2,change)# Una vez correctos, juntos las operaciones y numeros del camino desde n
    for elem in lista_2:#Añadimos las operaciones del segundo camino
        result= '(' + result + str(elem[1]) + str(elem[0]) + ')'
    return [long,result] #Tenemos la cantidad de numeros usados y la formula



#Resultado Global de Todo
#Esta parte se ejetuca sin necesidad de pedirlo por la terminal
file = open("TEST.txt","r")#Abrimos el archivo a leer "r"
goal= open("SCORE.txt","w")#Abrimos el archivo donde escribir "w"
x=datetime.datetime.now()# Esto es para el tiempo, no esta terminado
for line in file:#Para cada linea del archivo
    line=line.strip()#Quita cosas de la linea que no son necesarias
    fields = line.split("|")#Separa en elementos usando "|" como elemento de division 
    if fields[0] != 'ID' and fields[0] != "":#Si el primer elemento no es el ID ni una linea vacia 
        number = fields[1]; prime = fields[2]#Podemos coger el n y el p
        a,b,c,d=bfs(int(number),int(prime))#Y aplicar el algoritmo sobre ellos
        longitud,formula=display(a,b,c,d)#Sacamos los datos que tenemos que escribir
        goal.write('TicTac'+'|'+str(fields[0])+'|'+str(longitud)+'|'+str(formula)+'\n')#Y los escribimos en el archivo de salida
file.close(); goal.close() #Siempre al acabar se guardan los archivos cerrandolos


    
















