# -*- coding: utf-8 -*-

import collections

s = set([1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
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


def bfs( n, p):  
    dist={}
    ch={}
    ss=s.copy()
    ss.remove(p)
    q = collections.deque()
    for u in ss:
        dist[u]=[u]; ch[u]=[]
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
                        print(dist[w])
                        print(ch[w])
                        return w

    