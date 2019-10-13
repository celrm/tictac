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
const vector<ops> opsvec = {DIV,ADIV,MUL,SUM,RES,ARES};

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

// Busqueda en anchura.
// n es el destino, ss son los primos utilizables menos el restringido,
// cadena y ch guardan, para cada entero por el que pasamos, el estado
// en el que se encuentran la cadena de numeros y operaciones, respectivamente.
void bfs(ll n, mls &cadena,unordered_set<ll> &ss) {
	queue<pair<ll,int>> q; // La cola para guardar los nodos de cada nivel.
	unordered_map<ll,int> puntos;
	unordered_map<int,unordered_set<ll>> pool;
	for (auto u : ss) { // Todos los primos permitidos tienen como cadena ellos mismos.
		cadena[u] = to_string(u);
		puntos[u] = 1;
		q.push({u,1});
		if(u==n) return; // Se comprueba si hemos llegado al resultado.
	}
	pool[1] = ss; // Los del nivel 1.
	while (!q.empty()) {
		auto pair = q.front(); q.pop();
		u = pair.first;
		if(pair.second > 1) q.push({u,pair.second-1}); // Duran en la cola.
		for (int i = 1; i <= pair.second+1; ++i) { // Itero sobre los numeros que ya hemos calculado
		for (auto v : )
		for (auto o : opsvec) { // y sobre cada operacion.
			if(!(o==DIV && (v==0 || u%v!=0)) 
			&& !(o==ADIV && (u==0 || v%u!=0))) { // Condiciones de la division.
				ll w = op(u,v,o);
				if (cadena.find(w) == cadena.end()) { // Si aun no se ha pasado por w
					string sol = cadena[u]; // La nueva cadena es la anterior
					if (o==DIV || o==ADIV  || o==MUL || o==RES || o==ARES) { // mas parentesis
						sol = "(" + sol + ")";
					}
					if (o==ADIV || o==ARES) { // Caso no conmutativo.
						sol = cadena[v] + tochar(o) + sol;
					}
					else {
						sol = sol + tochar(o) + cadena[v];
					}
					cadena[w] = sol;
					if(w==n) return; // Se comprueba si hemos llegado al resultado.
					
					q.push(w); // Se guarda el nodo en la cola.
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
	
	unordered_set<ll> ss = s;
	ss.erase(p); // Se elimina de s el primo restringido.
	
	bfs(n,cadena,ss);
	
	cout << cadena[n];
	
	cout << '\n';
	
	return true;
}

int main() {
	while(caso());
}
