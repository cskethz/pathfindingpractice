def unv_min(unvisited, dist):
    store = [num if str(idx) in unvisited else float('inf') for idx,num in enumerate(dist)]
    
    return store.index(min(store))

def dijkstra(graph, source):

    unvisited = [str(i) for i in range(len(graph))]

    dist = [float('inf') for i in range(len(graph))]
    dist[source] = 0

    prev = [None for i in range(len(graph))]

    while unvisited:
        # implement a function to ignore visited nodes
        curr_node = unv_min(unvisited, dist)
        # remove current node
        unvisited.remove(str(curr_node))

        for node, length in enumerate(graph[curr_node]):
                if length > 0:
                        prev[node] = curr_node
                        alt = dist[curr_node] + length
                        if alt < dist[node]:
                            dist[node] = alt
        
    return dist

# List of connections between each node
graph = [[0, 2, 6, 0, 0, 0, 0], 
[2, 0, 0, 5, 0, 0, 0], 
[6, 6, 0, 8, 0, 0, 0], 
[0, 0, 8, 0, 10, 15, 0], 
[0, 0, 0, 10, 0, 6, 2], 
[0, 0, 0, 15, 6, 0, 6], 
[0, 0, 0, 0, 2, 6, 0]]; 

# Where the source node is
source = 0

if __name__ == "__main__":
    print(dijkstra(graph, source))
