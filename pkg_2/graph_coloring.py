from TdP_collections.graphs.graph import Graph
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue
from ReverseHeap import ReverseHeapPriorityQueue
from pkg_1.AdjListGraph import AdjListGraph

def graph_coloring(G):
    """preso in input un grafo G, restituisce un dizionario colors contenente una K-colorazione di G, utilizzando al
        più D+1 colori, dove D è il grado massimo dei vertici di G"""

    color = {}
    pq = ReverseHeapPriorityQueue()
    for v in G.vertices():
        degv = G.degree(v)
        pq.add(degv, v)                             #Riordino i vertici per grado decrescente

    ku = set()
    k = 0                                           #k tiene traccia del numero di colori usati, è una variabile di comodo
                                                    #usata per non dover richiamare ogni volta len() su ku
    while not pq.is_empty():
        deg, u = pq.remove_min()
        used = set()                                    #ad ogni iterazione controllo se il vertice corrente
        for v in color:                                 #è adiacente ad uno di quelli già nella soluzione. Se
            if G.get_edge(u, v):                        #questo è vero, tolgo dal set dei possibili colori che posso assegnare
                used.add(color[v])                      #a quel vertice il colore assegnato al vertice adicente
            elif G.is_directed() and G.get_edge(v,u):   #Nel caso in cui il grafo fosse diretto, devo controllare anche la
                used.add(color[v])                      #connessione inversa fra i due vertici in esame
        unused = ku.difference(used)
        if unused:
            color[u] = unused.pop()                     #se ci sono colori non utilizzati, ne assegno uno qualsiasi al vertice
        else:                                           #se l'insieme dei colori non utilizzati è vuoto, ne uso uno nuovo
            k += 1
            ku.add(k)
            color[u] = k
    return color

def print_coloring(colors, g):
    """preso in input un grafo g ed una sua colorazione, stampa le seguenti informazioni:
        -Numero di colori utilizzati
        -Colore assegnato ad ogni vertice
        -la coppia di colori assegnati ai vertici adiancenti ad ogni arco"""

    n_color = 0
    print("\tvertice\t|\tcolore \t\t\t")

    for v in colors:
        print("\t ",v,"\t|\t ",colors[v])
        n_color = max(colors[v],n_color)
    print("\n\n")
    print(" Colore \t\t Arco \t\t  Colore ")
    print("Sorgente \t\t   \t\t\tDestinazione")
    for e in g.edges():
        u,v = e.endpoints()
        print("\t",color[u]," \t|\t ",e.element(),"  \t|\t",colors[v])
    print("\n\n")
    print("Colori Utilizzati: \t",n_color)

###### Funzione di Test ################################################################################
def check_colors(G, color):
    """Ricevuti in ingresso un grafo ed una sua colorazione, controlla che non ci siano vertici adiacenti dello stesso
        colore"""
    for u in G.vertices():
        for e in G.incident_edges(u):
            v = e.opposite(u)
            if color[u] == color[v]:
                print(u,'\t',v)
                return False
    return True


def load_graph(file, directed=False):
    """legge da file un grafo rappresentato dalla lista dei suoi archi e costruisce (e restituisce) un oggetto 
    della classe Graph. Gli archi sono rappresentati come triple (sorgente, destinazione, elemento=1), 
    dove elemento è inizializzato per default a 1 se non presente."""
    g = AdjListGraph(directed)
    for line in file:
        edge = line.split()
        u = None
        v = None
        if len(edge) > 1:
            for k in g.vertices():
                if edge[0] == k.element():
                    u = k
                elif edge[1] == k.element():
                    v = k
                if u is not None and v is not None:
                    break

            if u is None:
                u = g.insert_vertex(edge[0])
            if v is None:
                v = g.insert_vertex(edge[1])
            if len(edge) == 3:
                g.insert_edge(u, v, edge[2])
            else:
                g.insert_edge(u, v, 1)
    return g

def max_degree(G):
    max_deg_out = 0
    max_deg_in = 0
    for v in G.vertices():
        degv = G.degree(v)
        max_deg_out = max(max_deg_out, degv)
        if G.is_directed():
            degv = G.degree(v, False)
            max_deg_in = max(max_deg_in, degv)
    return max(max_deg_in,max_deg_out)


if __name__ == '__main__':
    g = load_graph(open('grafo2.txt'), False)
    color= graph_coloring(g)
    print("check colors: ", check_colors(g, color))
    print("\nprint_coloring:")
    print_coloring(color,g)
    print("massimo grado del grafo:\t\t", max_degree(g))
