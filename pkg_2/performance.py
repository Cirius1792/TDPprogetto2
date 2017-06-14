from pkg_1.AdjListGraph import *
from pkg_2.graph_coloring import *
from TdP_collections.graphs.graph import *
import time

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
    N_Prove = 500;
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
        g = load_graph_g("C:\\Users\\Ciro Lucio\\PycharmProjects\\TDPprogetto2\\grafo2.txt", True)
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