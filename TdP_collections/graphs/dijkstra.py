from TDP.TdP_collections.priority_queue.adaptable_priority_queue import AdaptableHeapPriorityQueue

def shortest_path_lengths(g, src):
    """Calcola le distanze da src a tu2 gli altri ver5ci di g. Il grafo g può essere sia dire;o che
    indire;o ma deve essere pesato. Res5tuisce un dizionario che mappa ogni ver5ce
    raggiungibile da src nell sua distanza dal nodo di partenza."""
    d = {}                              # d[v] è un limite superiore alla distanza tra src e v
    cloud = {}                          # dizionario che mappa v in d[v]
    pq = AdaptableHeapPriorityQueue()   # ver5ce v avrà key d[v]
    pqlocator = {}                      # dizionario che mappa un ver5ce nel suo pq locator
    for v in g.vertices():               # per ogni ver5ce v calcola d[v] e inserisce v nella pq
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')         # sintassi per +∞
        pqlocator[v] = pq.add(d[v], v)  # salva il locator per I futuri aggiornamenti
    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key                  # inserisce u nella soluzione
        del pqlocator[u]                # cancella u dall pq
        for e in g.incident_edges(u):   # per tutti gli archi uscenti da u
            v = e.opposite(u)
            if v not in cloud:          # se v non è nella soluzione rilassa arco (u, v)
                wgt = float(e.element())
                if d[u] + wgt < d[v]:
                    d[v] = d[u] + wgt
                    pq.update(pqlocator[v], d[v], v)  # aggiorna d[v] nella pq
    return cloud  # la soluzione con5ene solo le distanze dai ver5ci raggiungibili


def shortest_path_tree(g, s, d):
    """Ricostruisce l’albero dei cammini minimi da s, date le distanze contenute nel dizionario
    d. Res5tuisce l’albero come una mappa che ad ogni vertice v raggiungibile associa l’arco
    (u, v) che collega v al padre nell’albero."""

    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, False):    # considera solo archi entran5
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:
                    tree[v] = e                     # l’arco è è stato u5lizzato per raggiungere v
    return tree
