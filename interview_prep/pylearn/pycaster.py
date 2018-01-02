from collections import deque

class Graph(object):

    def __init__(self, adj):
        self._adjacency_list = adj

    @property
    def adjacency_list(self):
        return self._adjacency_list
    
    @adjacency_list.setter
    def adjacency_list(self, value):
        pass
    
    @adjacency_list.deleter
    def adjacency_list(self):
        pass

    @staticmethod
    def bfs(graph, root, visit=None):
        seen = { root }
        queue = deque([root])
        path = []

        while queue:
            vertex = queue.pop()
            path.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in seen:
                    queue.appendleft(neighbor)
                    seen.add(neighbor)

        return path

    @staticmethod
    def dfs(graph, root, visit=None):
        seen = { root }
        stack = deque([root])
        path = []

        while stack:
            vertex = stack.pop()
            path.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in seen:
                    stack.append(neighbor)
                    seen.add(neighbor)

        return path

if __name__ == '__main__':
    graph = {'A': {'B', 'C'},
             'B': {'A', 'D', 'E'},
             'C': {'A', 'F'},
             'D': {'B'},
             'E': {'B'},
             'F': {'C'}
             }

    start = 'A'
    print("DFS Ordering: {}".format(Graph.dfs(graph, start)))
    print("BFS Ordering: {}".format(Graph.bfs(graph, start)))

