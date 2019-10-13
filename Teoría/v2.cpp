#include <iostream>
#include <climits>
#include <unordered_set>
#include <unordered_map>
#include <vector>
#include <list>
#include <queue>
#include <string>

using namespace std;
using ll = long long int;
using mls=unordered_map<ll,string>;

// Conjunto de primos utilizables.
const unordered_set<ll> s = {1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97};

// Para poder switchear e iterar sobre las operaciones
// las convierto tanto en enumerado como en vector.
// Cuidado, redundancia.
enum ops {DIV,ADIV,MUL,SUM,RES,ARES};
const vector<ops> opsvec = {MUL,SUM,RES,ARES,DIV,ADIV};

// Del enum a caracter.
char tochar(ops o) {
	switch(o) {
		case DIV	: return '/';
		case ADIV	: return '/';
		case MUL	: return '*';
		case SUM	: return '+';
		case RES	: return '-';
		case ARES	: return '-';
		default		: return '0';
	}
}

// Realizar la operacion entre u y v dada por o.
ll op(int u, int v, ops o) {
	switch(o) {
		case DIV	: return u/v;
		case ADIV	: return v/u;
		case MUL	: return u*v;
		case SUM	: return u+v;
		case RES	: return u-v;
		case ARES	: return v-u;
		default		: return 0;
	}
}

// Busqueda por nivel.
// n es el destino, ss son los primos utilizables menos el restringido,
// cadena y ch guardan, para cada entero por el que pasamos, el estado
// en el que se encuentran la cadena de numeros y operaciones, respectivamente.
void bfs(ll n, mls &cadena,unordered_map<ll,int> &puntos,unordered_set<ll> &ss) {
	unordered_map<int,unordered_set<ll>> pool;
	unordered_map<ll,bool> parentesis;
	
	int l = 1;
	
	for (auto u : ss) { // Todos los primos permitidos tienen como cadena ellos mismos.
		cadena[u] = to_string(u);
		parentesis[u] = false;
		puntos[u] = l;
		if(u==n) return; // Se comprueba si hemos llegado al resultado.
	}
	pool[l] = ss; // Los del nivel 1.
	
	for (l = 2; l < INT_MAX; ++l) { // Sabemos que siempre hay solucion asi que acaba.
	for (int i = l-1; i >= l/2+l%2; --i) {
		for(auto u : pool[i]) {
		for(auto v : pool[l-i]) {
			for (auto o : opsvec) {
				if(!(o==DIV && (v==0 || u%v!=0)) 
				&& !(o==ADIV && (u==0 || v%u!=0))) { // Condiciones de la division.
					ll w = op(u,v,o);
					if(cadena.find(w) == cadena.end()) { // Si aun no se ha pasado por w
						string cadu = cadena[u];
						string cadv = cadena[v];
						string sol;
						if(o==DIV || o==ADIV) { // Parentesis.
							if(puntos[u]>1) cadu = "(" + cadu + ")";
							if(puntos[v]>1) cadv = "(" + cadv + ")";							
						} if(o==MUL || o==RES || o==ARES) {
							if(!(o==RES) && parentesis[u]) cadu = "(" + cadu + ")";
							if(!(o==ARES) && parentesis[v]) cadv = "(" + cadv + ")";							
						}
						if (o==ADIV || o==ARES) // Caso no conmutativo.
							sol = cadv + tochar(o) + cadu;
						else
							sol = cadu + tochar(o) + cadv;
						cadena[w] = sol;
						parentesis[w] = (o==SUM || o==RES || o==ARES);
						puntos[w] = l;
						if(w==n) return; // Se comprueba si hemos llegado al resultado.
						pool[l].insert(w); // Los del nivel l.
					}
				}
			}
		}
		}
	}
	}
}

bool caso() {
	ll n,p; // n es el numero destino, p el primo restringido.
	cin >> n >> p;
	
	mls cadena;
	unordered_map<ll,int> puntos;
	
	unordered_set<ll> ss = s;
	ss.erase(p); // Se elimina de s el primo restringido.
	
	bfs(n,cadena,puntos,ss);
	
	cout << cadena[n];
	
	cout << '\n';
	
	for(auto v : puntos) {
		cout << v.first << " -> " << v.second << '\n';
	}
	
	return true;
}

int main() {
	while(caso());
}
