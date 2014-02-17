# @EXPECTED_RESULTS@: CORRECT

from sys import stdin, exit

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

    def __dfs(self, current, visits):
        if self.visited[current]:
            return

        self.visited[current] = True

        for next in xrange(self.num_nodes):
            if self.graph[current][next]:
                self.__dfs(next, visits)

        visits.append(current)

    def __rdfs(self, current):
        if self.visited[current]:
            return

        self.visited[current] = True

        for next in xrange(self.num_nodes):
            if self.graph[next][current]:
                self.__rdfs(next)

    def __has_cycle(self):
        for var in xrange(self.num_vars):
            if self.visited[self.__get_index(var, True)] and \
                    self.visited[self.__get_index(var, False)]:
                return True

        return False

n = int(stdin.readline())
p = SATProblem(3*n)

def get_possible_trucks(city):
    if city == 'Kristiansand':
        return (0, 2)
    elif city == 'Bergen':
        return (0, 1)
    elif city == 'Trondheim':
        return (1, 2)

def get_var(package, truck):
    return package + n*truck

for package, destination, line in zip(xrange(n), stdin.readline().split(), stdin):
    truckA, truckB = get_possible_trucks(destination)
    incompatibilities = map(int, line.split())

    # make sure we get on one of the two possible trucks
    p.add_clause(get_var(package, truckA), True, get_var(package, truckB), True)

    # make sure incompatible packages don't get on the same truck
    for truck in xrange(3):
        for incomp in incompatibilities:
            p.add_clause(get_var(package, truck), False, get_var(incomp, truck), False)

print 'Possible' if p.is_satisfiable() else 'Impossible'
