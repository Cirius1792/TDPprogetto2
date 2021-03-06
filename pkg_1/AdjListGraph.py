class AdjListGraph:
    """Representation of a simple graph using an adjacency list."""

    # ------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'

        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = x

        def element(self):
            """Return element associated with this vertex."""
            return self._element

        def __hash__(self):  # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

    # ------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return self._origin, self._destination

        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, AdjListGraph.Vertex):
                raise TypeError('v must be a Vertex')
            if v is self._origin:
                return self._destination
            elif v is self._destination:
                return self._origin

            raise ValueError('v not incident to edge')

        def element(self):
            """Return element associated with this edge."""
            return self._element

        def __hash__(self):  # will allow edge to be a map/set key
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

    # ------------------------- Graph methods -------------------------
    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default).
    
        Graph is directed if optional parameter is set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing
        self._aux_list = []

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        """Return True if this is a directed graph; False if undirected.
    
        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing  # directed if maps are distinct

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        return len(self._aux_list)

    def edges(self):
        """Return an iteration of all edges of the graph."""
        for e in self._aux_list:
            yield e

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        for e in self._outgoing[u]:
            if e.opposite(u) is v:
                return e
        return None

    def degree(self, v, outgoing=True):
        """Return number of (outgoing) edges incident to vertex v in the graph.
    
        If graph is directed, optional parameter used to count incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """Return all (outgoing) edges incident to vertex v in the graph.
    
        If graph is directed, optional parameter used to request incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v]:
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = []
        if self.is_directed():
            self._incoming[v] = []  # need distinct map for incoming edges
        return v

    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.
    
        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u].append(e)
        self._incoming[v].append(e)
        self._aux_list.append(e)

    def find_vertex(self, v):
        """Find and return a vertex by label.
        Return None if vertex is not found."""
        for vertex in self.vertices():
            if vertex.element() == v:
                return vertex
        return None


def load_graph(path, directed=False):
    """Load a graph from a file, in witch each row is formatted as 'S D W' where:
    - S is the source vertex
    - D is the destination vertex
    - W is the weight of the edge (is set to 1 if not present)
    
    Return an AdjListGraph object.
    """
    in_file = open(path)

    graph = AdjListGraph(directed)

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
