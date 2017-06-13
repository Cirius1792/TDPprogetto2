from .ReverseHeap import ReverseHeapPriorityQueue


def graph_coloring(G):
    """Preso in input un grafo G, restituisce un dizionario colors contenente una K-colorazione di G, utilizzando al
        più D+1 colori, dove D è il grado massimo dei vertici di G"""

    color = {}
    pq = ReverseHeapPriorityQueue()
    for v in G.vertices():
        degv = G.degree(v)
        pq.add(degv, v)  # Riordino i vertici per grado decrescente

    ku = set()
    k = 0  # k tiene traccia del numero di colori usati, è una variabile di comodo
    # usata per non dover richiamare ogni volta len() su ku
    while not pq.is_empty():
        deg, u = pq.remove_min()
        used = set()  # ad ogni iterazione controllo se il vertice corrente
        for v in color:  # è adiacente ad uno di quelli già nella soluzione. Se
            if G.get_edge(u, v):  # questo è vero, tolgo dal set dei possibili colori che posso assegnare
                used.add(color[v])  # a quel vertice il colore assegnato al vertice adicente
            elif G.is_directed() and G.get_edge(v,
                                                u):  # Nel caso in cui il grafo fosse diretto, devo controllare anche la
                used.add(color[v])  # connessione inversa fra i due vertici in esame
        unused = ku.difference(used)
        if unused:
            color[u] = unused.pop()  # se ci sono colori non utilizzati, ne assegno uno qualsiasi al vertice
        else:  # se l'insieme dei colori non utilizzati è vuoto, ne uso uno nuovo
            k += 1
            ku.add(k)
            color[u] = k
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
