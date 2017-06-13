from pkg_2.graph_coloring import *
from pkg_3.enumerate_coloring import *


def check_colors(G, color):
    """Ricevuti in ingresso un grafo ed una sua colorazione, controlla che non ci siano vertici adiacenti dello stesso
        colore"""
    for e in G.edges():
        u, v = e.endpoints()
        if color[u] == color[v]:
            return False
    return True


def max_degree(G):
    """Dato un grafo in ingresso G, restituisce il massimo grado dei suoi vertici. Nel caso di grafi diretti,
    si considera la somma del grado entrante e di quello uscente"""
    max_deg = 0
    dir = G.is_directed()
    for v in G.vertices():
        degv = G.degree(v) if not dir else G.degree(v) + G.degree(v, False)
        max_deg = max(max_deg, degv)
    return max_deg


if __name__ == '__main__':
    print("\n\n----------------------------------------------------------------")
    print('------------------ Gruppo #10 - Test ---------------------------')
    print("----------------------------------------------------------------")

    g = load_graph("C:\\Users\\CiroLucio\\PycharmProjects\\progetto2\\grafo1.txt", True)

    print('\nNumero di vertici nel grafo: ', g.vertex_count())
    print('Numero di archi nel grafo: ', g.edge_count())
    print("Massimo grado del grafo:\t", max_degree(g))

    print('\n\n--------- Test Graph Coloring --------')
    color = graph_coloring(g)
    if check_colors(g, color):
        print('\nColorazione avvenuta con successo')
    else:
        print('\nColorazione errata')

    print_coloring(color, g)

    print('\n\n--------- Test Enumerate Coloring --------')
    k = 4
    l_col = enumerate_coloring(g, k)
    if l_col is not None:
        print('\nNumero totale di k-colorazioni, con k=',k, 'è: ', len(l_col), '\n')
        print_coloring_list(g, l_col)
    else:
        print('Non è possibile colorare il grafo con', k, 'colori!')

    #print('\nIl minor numero di colori necessari per colorare il grafo è:', min_colors(g))
