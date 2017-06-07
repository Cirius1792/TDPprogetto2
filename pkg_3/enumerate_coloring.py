from pkg_1.AdjListGraph import *


def enumerate_coloring(g: AdjListGraph, k):
    vert = list(g.vertices())
    l_col = []
    d = {}
    _backtrack_coloring(g, vert, 0, d, k, l_col)
    return l_col if len(l_col) != 0 else None


def _backtrack_coloring(g, vert, ind, d, k, l_col):
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
    for i in range(k):
        if i not in s:
            c = d.copy()
            c[vert[ind]] = i
            _backtrack_coloring(g, vert, ind + 1, c, k, l_col)


def min_colors(g):
    k = 1
    while True:
        if enumerate_coloring(g, k):
            return k
        k += 1




g = load_graph('../7.3.txt', True)


l = enumerate_coloring(g, 3)
print(len(l))
print()
for d in l:
    print('-----Dizionario------')
    for elem in d:
        print(elem, d[elem])

print('\nColore minimo = ', min_colors(g))
