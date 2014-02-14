# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

class SATProblem:
    def __init__(self, num_vars):
        self.num_vars = num_vars
        self.num_nodes = 2*num_vars + 1

        self.graph = [[0]*self.num_nodes for i in xrange(self.num_nodes)]
        self.visited = [False]*self.num_nodes

    def add_clause(self, lhs, lpred, rhs, rpred):
        a = self.__get_index(lhs, not lpred)
        b = self.__get_index(rhs, rpred)
        self.graph[a][b] = True

        a = self.__get_index(rhs, not rpred)
        b = self.__get_index(lhs, lpred)
        self.graph[a][b] = True

    def is_satisfiable(self):
        visits = []

        for node in xrange(self.num_nodes):
            self.__dfs(node, visits)

        self.visited = [False]*self.num_nodes

        while len(visits):
            self.__rdfs(visits.pop())

            if self.__has_cycle():
                return False

            for i in xrange(self.num_nodes):
                if self.visited[i]:
                    self.__remove_node(i)
                    self.visited[i] = False

        return True

    def __get_index(self, var, pred):
        return (var+1) if pred else (self.num_nodes - (var+1))

    def __remove_node(self, node):
        self.graph[node] = [False]*self.num_nodes

    def __dfs(self, root, visits):
        to_visit = [root]

        while to_visit:
            current = to_visit.pop()

            if self.visited[current]:
                continue

            self.visited[current] = True

            for next in xrange(self.num_nodes):
                if self.graph[current][next] and not self.visited[next]:
                    to_visit.append(next)

            visits.append(current)

    def __rdfs(self, root):
        to_visit = [root]

        while to_visit:
            current = to_visit.pop()

            if self.visited[current]:
                continue

            self.visited[current] = True

            for next in xrange(self.num_nodes):
                if self.graph[next][current] and not self.visited[next]:
                    to_visit.append(next)

    def __has_cycle(self):
        for var in xrange(self.num_vars):
            if self.visited[self.__get_index(var, True)] and \
                    self.visited[self.__get_index(var, False)]:
                return True

        return False

n = int(stdin.readline())
p = SATProblem(n)

citymap = {'Kristiansand':0, 'Bergen':1, 'Trondheim':2}
destinations = [citymap[city] for city in stdin.readline().split()]

for package, line in zip(xrange(n), stdin):
    incompatibilities = map(int, line.split())

    p_dest = destinations[package]

    for incomp in incompatibilities:
        i_dest = destinations[incomp]

        if p_dest == i_dest:
            p.add_clause(package, True, incomp, True)
            p.add_clause(package, False, incomp, False)
        elif (i_dest - p_dest) % len(citymap) == 1:
            p.add_clause(package, True, incomp, False)
        else:
            p.add_clause(package, False, incomp, True)

print 'Possible' if p.is_satisfiable() else 'Impossible'
