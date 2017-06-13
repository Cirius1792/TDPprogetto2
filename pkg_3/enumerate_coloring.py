from pkg_1.AdjListGraph import *


def enumerate_coloring(g: AdjListGraph, k):
    """Dato in input un	AdjListGraph ed	un intero k, restituisce tutte le k-colorazioni	del	grafo."""
    vert = list(g.vertices())
    l_col = []
    d = {}
    _backtrack_coloring(g, vert, 0, d, k, l_col)
    return l_col if len(l_col) != 0 else None


def _backtrack_coloring(g, vert, ind, d, k, l_col):
    """Funzione di backtracking ausiliaria per il calcolo delle k_colorazioni"""
    if ind == len(vert):
        l_col.append(d)
        return
    l = []
    for e in g.incident_edges(vert[ind]):
        l.append(e.opposite(vert[ind]))
    if g.is_directed():
        for e in g.incident_edges(vert[ind], False):
            l.append(e.opposite(vert[ind]))
    s = set()
    for elem in l:
        if elem in d:
            s.add(d[elem])
    if len(s) == k:
        return
    for i in range(1, k + 1):
        if i not in s:
            c = d.copy()
            c[vert[ind]] = i
            _backtrack_coloring(g, vert, ind + 1, c, k, l_col)


def min_colors(g):
    "Dato in input un	AdjListGraph g, calcola	il	minor numero di	colori	necessari per colorare il grafo."
    k = 1
    while True:
        if enumerate_coloring(g, k):
            return k
        k += 1


def print_coloring_list(g, l):
    print(' ' * 20 + '+' + ('-' * 7 + '+') * g.vertex_count())
    print('\t\t\t\t\t|', end='')
    for v in g.vertices():
        print('{:^7}'.format(str(v)) + '|', end='')
    print()
    print('+' + '-' * 19 + '+' + ('-' * 7 + '+') * g.vertex_count())
    count = 1
    for col in l:
        print('| Colorazione', count, '\t|', end='')
        for v in col:
            print('{:^7}'.format(str(col[v])) + '|', end='')
        print()
        count += 1
        print('+' + '-' * 19 + '+' + ('-' * 7 + '+') * g.vertex_count())
