# @EXPECTED_RESULT@: CORRECT

from sys import stdin;

class Solver:

	def __init__(self):
		self.read_parameters();
		self.read_walls();

	def read_parameters(self):
		line = stdin.next();
		par = line.split();
		self.M = int(par[0]); self.N = int(par[1]);
		self.I = int(par[2]);

	def read_walls(self):
		M = self.M; N = self.N;
		self.vertical = [];
		self.horizontal = [];
	
		for y in range(N):
			line = stdin.next();
			self.vertical.append([int(w) for w in line.split()]);
		for y in range(N-1):
			line = stdin.next();
			self.horizontal.append([int(w) for w in line.split()]);

	def cell_str(self, m, n):
		#print("m=%i, n=%i" %(m,n));
		s = '';
		s += self.under_str(m,n);
		s += self.right_str(m,n);
		return s;

	def right_str(self, m, n):
		if(m+1 >= self.M):
			return '';
		if(self.vertical[n][m] == 1):
			return '|';
		return ':';

	def under_str(self, m, n):
		if(n+1 >= self.N):
			return '.';
		if(self.horizontal[n][m] == 1):
			return '_';
		return '.';

	def pprint(self):
		for n in range(self.N):
			line = '';
			for m in range(self.M):
				line += self.cell_str(m,n);
			print(line);

sol = Solver();
sol.pprint();
