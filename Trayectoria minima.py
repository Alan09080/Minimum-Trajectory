import os
import networkx as nx
import matplotlib.pyplot as plt

#   CREAR UN GRAFO DIRIGIDO, PARA ELLO EL USUARIO INGRESA EL NUMERO DE
#   VERTICES Y EL NUMERO DE ARISTAS. SE CREA UN DICCIONARIO VACIO
#   EN EL CUAL SE GUARDAN LOS VERTICES


def crearGrafoDirigido(n_vertices, n_aristas):
    grafo = {}
    for i in range(n_vertices):
        grafo[i] = []
    for i in range(n_aristas):
        origen = int(input("Ingrese la luminaria de origen: "))
        destino = int(input("Ingrese la luminaria de destino: "))
        peso = float(input("Ingrese la distancia entre estas luminarias: "))
        grafo[origen].append((destino, peso))
    return grafo


#   A CONTINUACIÓN SE PIDE AL USUARIO QUE INGRESE EL VERTICE ORIGEN, EL VERTICE DESTINO
#   Y EL PESO DE LA ARISTA, ESTA INFORMACIÓN SERA GUARDADA EN EL DICCIONARIO
#   POR ULTIMO SE IMPRIME EL GRAFO CREADO

n_vertices = int(input("Ingrese el número de luminarias: "))
n_aristas = int(input("Ingrese el número de posibles conexiones entre ellas: "))
grafo = crearGrafoDirigido(n_vertices, n_aristas)
print(grafo)

listaVisitados = []
grafoResultante = {}
listaOrdenada = []

#    COMIENZO DEL ALGORITMO DE PRIM
# 1.- ELEGIR NODO ORIGEN AL AZAR O PEDIRLO AL USUARIO
origen = int(input("\nIngresa el número de la lampara de origen: "))
# 2.- AGREGARLO A LA LISTA DE VISITADOS
listaVisitados.append(origen)

# 3.- AGREGAR SUS ADYACENTES A LA LISTA ORDENADA
for destino, peso in grafo[origen]:
    listaOrdenada.append((origen, destino, peso))
"""ORDENAMIENTO INSERT PARA LA LISTA"""
pos = 0
act = 0
listAux = []
for i in range(len(listaOrdenada)):
    listAux = listaOrdenada[i]
    act = listaOrdenada[i][2]
    pos = i
    while pos > 0 and listaOrdenada[pos - 1][2] > act:
        listaOrdenada[pos] = listaOrdenada[pos - 1]
        pos = pos - 1
    listaOrdenada[pos] = listAux

# 4.- MIENTRAS LA LISTA ORDENADA NO ESTE VACIA, HACER:
while listaOrdenada:
    # 5.-TOMAR VERTICE DE LA LISTA ORDENADA Y ELIMINARLO
    vertice = listaOrdenada.pop(0)
    d = vertice[1]

    # 6.-SI EL DESTINO NO ESTA EN LA LISTA DE VISITADOS
    if d not in listaVisitados:
        # 7.- AGREGAR A LA LISTA DE VISITADOS EN NODO DESTINO
        listaVisitados.append(d)
        # 8.- AGREGAR A LA LISTA ORDENADA LOS ADYACENTES DEL NODO DESTINO
        # "d" QUE NO HAN SIDO VISITADOS
        for key, lista in grafo[d]:
            if key not in listaVisitados:
                listaOrdenada.append((d, key, lista))
        #####ORDENAMIENTO APLICADO A LA LISTA :
        listaOrdenada = [(c, a, b) for a, b, c in listaOrdenada]
        listaOrdenada.sort()
        listaOrdenada = [(a, b, c) for c, a, b in listaOrdenada]
        # 9.-AGREGAR VERTICE AL GRAFO RESULTANTE
        # PARA COMPRENDER MEJOR, EN LAS SIGUIENTES LINEAS SE TOMA EL "VERTICE", QUE EN ESTE CASO
        # ES UNA TUPLA QUE CONTIENE TRES VALORES; EL VERTICE EN SU POSICIÓN 0 ES EL VALOR DEL NODO ORIGEN
        # EL VÉRTICE EN SU POSICIÓN 1 ES EL NODO DESTINO, Y EL VÉRTICE EN SU POSICIÓN 2 ES EL PESO DE LA ARISTA ENTRE AMBOS NODOS,
        # Y A CONTINUACIÓN SE AGREGAN ESOS VALORES AL GRAFO
        origen = vertice[0]
        destino = vertice[1]
        peso = vertice[2]

        if origen in grafoResultante:
            if destino in grafoResultante:
                lista = grafoResultante[origen]
                grafoResultante[origen] = lista + [(destino, peso)]
                lista = grafoResultante[destino]
                lista.append((origen, peso))
                grafoResultante[destino] = lista
            else:
                grafoResultante[destino] = [(origen, peso)]
                lista = grafoResultante[origen]
                lista.append((destino, peso))
                grafoResultante[origen] = lista
        elif destino in grafoResultante:
            grafoResultante[origen] = [(destino, peso)]
            lista = grafoResultante[destino]
            lista.append((origen, peso))
            grafoResultante[destino] = lista
        else:
            grafoResultante[destino] = [(origen, peso)]
            grafoResultante[origen] = [(destino, peso)]

print("\n\nTrayectoria resultante:\n")
for key, lista in grafoResultante.items():
    print(key)
    print(lista)

#   ESTA FUNCIÓN ES UNA FUNCIÓN DE AYUDA PARA DIBUJAR UN GRAFO.
#   TOMA UN GRAFO COMO PARÁMETRO Y USA LA LIBRERÍA MATPLOTLIB PARA DIBUJARLO.
#   EL GRAFO SE DIBUJA CON UN LAYOUT CIRCULAR, LOS NODOS SE DIBUJAN CON ETIQUETAS,
#   LOS ARCOS SE DIBUJAN SIN FLECHAS Y LOS PESOS SE DIBUJAN COMO ETIQUETAS EN LOS ARCOS


def dibujarGrafo(grafo):
    G = nx.DiGraph()
    for origen, lista in grafo.items():
        for destino, peso in lista:
            G.add_edge(origen, destino, weight=peso)
    labels = nx.get_edge_attributes(G, "weight")
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=False, font_weight="bold")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


dibujarGrafo(grafoResultante)
