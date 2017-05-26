from TDP.TdP_collections.graphs.graph import Graph

def BellmaFord(G,s):

    d = {}

    for v in G.vertices():
       d[v] = 0 if v == s else float('inf')
    for i in range(len(G.vertices())-1):
        for e in G.edges():
            u, v = e.endpoints()
            wgt = float(e.element())
            if d[u] + wgt < d[v]:
                d[v] = d[u] + wgt
    return d