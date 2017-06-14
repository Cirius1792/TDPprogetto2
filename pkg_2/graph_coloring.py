from pkg_2.ReverseHeap import ReverseHeapPriorityQueue
from pkg_1.AdjListGraph import *
from TdP_collections.graphs.graph import *
import time

def graph_coloring_1(G):
    """Preso in input un grafo G, restituisce un dizionario colors contenente una K-colorazione di G, utilizzando al
        più D+1 colori, dove D è il grado massimo dei vertici di G"""
    color = {}
    pq = ReverseHeapPriorityQueue()
    for v in G.vertices():
        degv = G.degree(v)
        pq.add(degv, v)                         # Riordino i vertici per grado decrescente

    ku = set()
    k = 0                                       # k tiene traccia del numero di colori usati, è una variabile di comodo
                                                 # usata per non dover richiamare ogni volta len() su ku
    while not pq.is_empty():
        deg, u = pq.remove_min()
        used = set()                            # ad ogni iterazione controllo se il vertice corrente
        for v in color:                         # è adiacente ad uno di quelli già nella soluzione. Se
            if G.get_edge(u, v):                # questo è vero, tolgo dal set dei possibili colori che posso assegnare
                used.add(color[v])              # a quel vertice il colore assegnato al vertice adicente
            elif G.is_directed() and G.get_edge(v, u):         # Nel caso in cui il grafo fosse diretto, devo controllare anche la
                used.add(color[v])  # connessione inversa fra i due vertici in esame
        unused = ku.difference(used)
        if unused:
            color[u] = unused.pop()  # se ci sono colori non utilizzati, ne assegno uno qualsiasi al vertice
        else:  # se l'insieme dei colori non utilizzati è vuoto, ne uso uno nuovo
            k += 1
            ku.add(k)
            color[u] = k
            
    return color


def graph_coloring(G):
    """Preso in input un grafo G, restituisce un dizionario colors contenente una K-colorazione di G, utilizzando al

        più D+1 colori, dove D è il grado massimo dei vertici di G"""
    op = 0
    color = {}
    pq = ReverseHeapPriorityQueue()
    for v in G.vertices():
        degv = G.degree(v)
        pq.add(degv, v)                 # Riordino i vertici per grado decrescente
        op += 1
    ku = set()
    k = 0                               # k tiene traccia del numero di colori usati, è una variabile di comodo
                                        # usata per non dover richiamare ogni volta len() su ku
    while not pq.is_empty():
        deg, u = pq.remove_min()
        used = set()
        for e in G.incident_edges(u):
            v = e.opposite(u)
            if v in color:
                used.add(color[v])
            op += 1
        if G.is_directed():
            for e in G.incident_edges(u, False):
                v = e.opposite(u)
                if v in color:
                    used.add(color[v])
                op += 1
        unused = ku.difference(used)
        if unused:
            color[u] = unused.pop()         # se ci sono colori non utilizzati, ne assegno uno qualsiasi al vertice
        else:                               # se l'insieme dei colori non utilizzati è vuoto, ne uso uno nuovo
            k += 1
            ku.add(k)
            color[u] = k
        op += 1

    return color


def print_coloring(colors, g):
    """Preso in input un grafo g ed una sua colorazione, stampa le seguenti informazioni:
        - Numero di colori utilizzati
        - Colore assegnato ad ogni vertice
        - La coppia di colori assegnati ai vertici adiancenti ad ogni arco"""

    print("Colori Utilizzati: \t", max(colors.values()))
    print()
    print('+' + '-' * 11 + '+' + '-' * 11 + '+')
    print('|  Vertice\t|  Colore\t|')
    print('+' + '-' * 11 + '+' + '-' * 11 + '+')

    for v in colors:
        print('|' + '{:^10}'.format(str(v)), '|' + '{:^10}'.format(str(colors[v])), '|')
        print('+' + '-' * 11 + '+' + '-' * 11 + '+')

    print()

    print('+' + '-' * 17 + '+' + '-' * 9 + '+' + '-' * 21 + '+')
    print('| Colore Sorgente |\t Arco\t| Colore Destinazione |')
    print('+' + '-' * 17 + '+' + '-' * 9 + '+' + '-' * 21 + '+')

    for e in g.edges():
        u, v = e.endpoints()
        print('|' + '{:^16}'.format(str(colors[u])), '| ' + '{:^7}'.format(str(e)),
              '|' + '{:^20}'.format(str(colors[v])), '|')
        print('+' + '-' * 17 + '+' + '-' * 9 + '+' + '-' * 21 + '+')


def load_graph_g(path, directed=False):
    """Load a graph from a file, in witch each row is formatted as 'S D W' where:
    - S is the source vertex
    - D is the destination vertex
    - W is the weight of the edge (is set to 1 if not present)

    Return an AdjListGraph object.
    """
    in_file = open(path)

    graph = Graph(directed)

    for riga in in_file:
        v = riga.split()

        v_sor = graph.find_vertex(v[0])
        if v_sor is None:
            v_sor = graph.insert_vertex(v[0])
        v_dest = graph.find_vertex(v[1])
        if v_dest is None:
            v_dest = graph.insert_vertex(v[1])
        if len(v) == 3:
            graph.insert_edge(v_sor, v_dest, v[2])
        else:
            graph.insert_edge(v_sor, v_dest, 1)

    return graph

if __name__ == '__main__':
    adj_originale = {}
    adj_modificata = {}
    grp_originale = {}
    grp_modificata = {}
    N_Prove = 100;
    for i in range(N_Prove):
        g = load_graph("C:\\Users\\Ciro Lucio\\PycharmProjects\\TDPprogetto2\\grafo2.txt", False)
        start = time.time()
        color = graph_coloring_1(g)
        stop = time.time()
        t1 = stop - start
        adj_originale[i] = t1

        start = time.time()
        color = graph_coloring(g)
        stop = time.time()
        t2 = stop-start
        adj_modificata[i] = t2
        del g
        g = load_graph_g("C:\\Users\\Ciro Lucio\\PycharmProjects\\TDPprogetto2\\7.3.txt", True)
        start = time.time()
        color = graph_coloring_1(g)
        stop = time.time()
        t1 = stop - start
        grp_originale[i] = t1
        start = time.time()
        color = graph_coloring(g)
        stop = time.time()
        t2 = stop-start
        grp_modificata[i] = t2

        del g
    me_adj_originale = 0
    me_adj_modificata = 0
    me_grp_originale = 0
    me_grp_modificata = 0
    cnt = 0
    for i in grp_originale:
        cnt += 1
        me_adj_originale += adj_originale[i]
        me_adj_modificata += adj_modificata[i]
        me_grp_originale += grp_originale[i]
        me_grp_modificata += grp_modificata[i]
    me_adj_originale /= cnt
    me_adj_modificata /= cnt
    me_grp_originale /= cnt
    me_grp_modificata /= cnt

    print("prestazioni con adj list")
    print("versione originale: \t", me_adj_originale)
    print("versione modificata: \t",me_adj_modificata)
    print("\nprestazioni classe graph")
    print("versione originale: \t", me_grp_originale)
    print("versione modificata: \t",me_grp_modificata)