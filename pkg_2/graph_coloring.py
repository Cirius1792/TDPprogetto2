from TdP_collections.graphs.graph import Graph
from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue


def graph_coloring(G):

    color = {}
    pq = HeapPriorityQueue()
    for v in G.vertices():
        degv = G.degree(v)
        pq.add(degv, v)                         #Riordino i vertici per grado crescente

    ku = set()
    k = 0
    while not pq.is_empty():
        deg, u = pq.remove_min()
        used = set()                            #ad ogni iterazione controllo se il vertice corrente
        for v in color:                         #è adiacente ad uno di quelli già nella soluzione. Se
            if G.get_edge(u, v):                #questo è vero, tolgo dal set dei possibili colori che posso assegnare
                used.add(color[v])              #a quel vertice il colore assegnato al vertice adicente
        unused = ku.difference(used)
        if unused:
            color[u] = unused.pop()
        else:
            k += 1
            ku.add(k)
            color[u] = k
    return color

def print_coloring(colors, g):
    n_color = 0
    for v in colors:
        print("vertice:\t\t\t ",v,"\t\tcolore: \t\t\t",colors[v])
        n_color = max(colors[v],n_color)
    for e in g.edges():
        u,v = e.endpoints()
        print(color[u],"\t ",e,"  \t",colors[v])
    print("colori utilizzati: \t",n_color)

def check_colors(G, color):
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
    g = Graph(directed)
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
    if G.is_directed():
        print("max_deg_in:\t",max_deg_in,"max_deg_out:\t",max_deg_out)
    else:
        print("max_deg_out:\t",max_deg_out)
    return max(max_deg_in,max_deg_out)


if __name__ == '__main__':
    g = load_graph(open('grafo1.txt'), True)
    color= graph_coloring(g)
    print("check colors: ", check_colors(g, color))
    D = max_degree(g)
    print("max degree:\t\t",D)
    print("\nprint_coloring:")
    print_coloring(color,g)