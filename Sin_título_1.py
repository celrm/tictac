# -*- coding: utf-8 -*-


"""
Traduccion del algoritmo a Python (incompleta)

debería funcionar correctamente pero hay un problema en algun lado que estoy buscando
"""


import collections

s = set((1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97))
ops={"*","+","-","/"}

def op( u, v, o):
    if o=="*":
        return u*v
    elif o=="+":
        return u+v
    elif o=="-":
        return u-v
    elif o=="/" and u%v==0:
        return u/v


dist={}
ch={}

def bfs( n, dist, ch, ss):
    q = collections.deque()
    for u in ss:
        dist[u]=[u]; ch[u]=[u]
        q.append(u)
    while len(q)!=0:
        u = q[0]
        q.popleft()
        if u==n:
            return
        for v in ss:
            for o in ops:
                w=op(u,v,o)
                if w in dist.keys() and w!=None and w>0:
                    aux= dist[u]
                    aux.insert(0,v)
                    if len(aux)<len(dist[w]):
                        dist[w] = aux
                if w not in dist.keys() and w!=None and w>0:
                    dist[w] = dist[u]
                    dist[w].insert(0,v)
                    ch[w] = ch[u]
                    ch[w].insert(0,o)
                    q.append(w)


def funcion(n,p):
    ss=s
    ss.remove(p)
    bfs(n, dist, ch, ss)




