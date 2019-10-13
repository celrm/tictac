# -*- coding: utf-8 -*-

import collections

s = set([1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
primes=[1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
ops={"*","+","-","/"}


def op( u, v, o):
    if o=="*":
        return u*v
    if o=="+":
        return u+v
    if o=="-":
        return u-v
    if o=="/" and u%v==0:
        return int(u/v)


def factors(n, startFrom=2):
    if n <= 1:  return [ ]
    d = startFrom
    factors = [ ]
    while n >= d*d:
      if n % d == 0:
        factors.append(d)
        n = n/d
      else:
        d += 1 + d % 2
    factors.append(n)
    return factors


def bfs( n, p):  
    dist={}
    ch={}
    ss=s.copy()
    ss.remove(p)
    q = collections.deque()
    for u in ss:
        dist[u]=[u]; ch[u]=[]
        if u==n:
            return [dist[u],ch[u]]
        q.append(u)
    while len(q)!=0:
        u = q[0]
        q.popleft()
        for v in ss:          
            for o in ops:
                w=op(u,v,o)
                if w in dist.keys()and w!=None and w>0:
                    aux= dist[u].copy()
                    aux.append(v)
                    if len(aux)<len(dist[w]):
                        dist.update({w:aux})
                        ch[w] = ch[u].copy()
                        ch[w].append(o)  
                if w not in dist.keys() and w!=None and w>0:
                    dist[w]= dist[u].copy()
                    dist[w].append(v)
                    ch[w] = ch[u].copy()
                    ch[w].append(o)
                    q.append(w)
                    if w==n:
                        return [dist[w],ch[w]]

""" Si hay muchos factores del mismo numero los junta y aplica el algoritmo sobre ellos"""
def funcion(n,p):
    if n>500000:
        result=[]
        lista=factors(n)
        for prime in primes:
            ocur=lista.count(prime)
            if ocur>2:
                lista=list(filter((prime).__ne__, lista))
                lista.append(prime**ocur)
        for i in lista:
            a=funcion(i,p)
            result.append(a)
        return result
    else:
        return bfs( n, p)






