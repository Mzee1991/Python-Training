# A simple representation of graph using STL,
# for the purpose of competitive programming

# A utility function to add an edge in an
# undirected graph.
def addEdge(adj, u, v):
	adj[u].append(v)
	adj[v].append(u)
	return adj

# A utility function to do DFS of graph
# recursively from a given vertex u.
def DFSUtil(u, adj, visited):
	visited[u] = True
	print(u, end = " ")
	for i in range(len(adj[u])):
		if (visited[adj[u][i]] == False):
			DFSUtil(adj[u][i], adj, visited)

# This function does DFSUtil() for all
# unvisited vertices.
def DFS(adj, V):
	visited = [False]*(V+1)

	for u in range(V):
		if (visited[u] == False):
			DFSUtil(u, adj, visited)

# Driver code
if __name__ == '__main__':
	V = 5

	# The below line may not work on all
	# compilers. If it does not work on
	# your compiler, please replace it with
	# following
	# vector<int> *adj = new vector<int>[V]
	adj = [[] for i in range(V)]

	# Vertex numbers should be from 0 to 4.
	adj = addEdge(adj, 0, 1)
	adj = addEdge(adj, 0, 4)
	adj = addEdge(adj, 1, 2)
	adj = addEdge(adj, 1, 3)
	adj = addEdge(adj, 1, 4)
	adj = addEdge(adj, 2, 3)
	adj = addEdge(adj, 3, 4)
	DFS(adj, V)

# This code is contributed by mohit kumar 29.

