# @EXPECTED_RESULT@:

from sys import stdin;

class Solver:

	def __init__(self):
		self.read_parameters();
		self.read_walls();

	def read_parameters(self):
		line = stdin.next();
		par = line.split();
		self.X = int(par[0]); self.Y = int(par[1]);
		self.M = int(par[2]);

	def read_walls(self):
		X = self.X; Y = self.Y;
		self.vertical = [];
		self.horizontal = [];
		self.dp = [[0 for x in range(X)] for y in range(Y)];
		self.dp[0][0] = self.M;
	
		for y in range(Y):
			line = stdin.next();
			self.vertical.append([int(w) for w in line.split()]);
		for y in range(Y-1):
			line = stdin.next();
			self.horizontal.append([int(w) for w in line.split()]);

	def calc_opt(self, x,y):
		if(x == 0 and y == 0):
			return;
		self.dp[y][x] = max(self.left(x,y), self.over(x,y),0);

	def over(self, x, y):
		if(y == 0):
			return 0;
		return self.dp[y-1][x]-self.horizontal[y-1][x];

	def left(self,x,y):
		if(x==0):
			return 0;
		return self.dp[y][x-1] -self.vertical[y][x-1];

	def ans(self):
		for x in range(self.X):
			for y in range(self.Y):
				self.calc_opt(x,y);
		return self.dp[-1][-1];


sol = Solver();
print(sol.ans());
