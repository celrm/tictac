# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:43:20 2019

@author: Familia
"""

import time
import collections

def op( u, v, o): 
    if o=="*":
        return u*v
    if o=="+":
        return u+v
    if o=="-":
        return u-v
    if o=="/" and u%v==0:
        return int(u/v)


s = set([1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]) 
ops={"*","+","-","/"}


def bfs( n, p):
    print(time.time())
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
                            print(time.time())
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
                            print(time.time())
                            return [dist[y],ch[y],dist_inv[y],ch_inv[y]]
                    
                    
                    
                    
                
                
                
                
                
                
                
                
                
                
                