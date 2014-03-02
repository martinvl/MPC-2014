#Inefficient sol. using O(XY) memory
from sys import stdin;
import numpy as np;

class Solver:

	def __init__(self,X,Y,M, board):
		self.X = X; self.Y = Y; self.M = M;
		self.board = board;

		#should inverse dimensions in problem statement?
		self.dp = np.array([[0 for y in range(Y)] for x in range(X)]);
		
		self.dp[0][0] = M+1;

	def good_under(self,i,j):
		if(i == 0):
			return False;
		if(self.board[i][j] == '1' and 
				self.board[i-1][j] == '1'):
			return False;
		return True;

	def good_left(self,i,j):
		if(j == 0):
			return False;
		if(self.board[i][j] == '1' and
				self.board[i][j-1] == '1'):
			return False;
		return True;

	def calc_max(self, i,j):
		if(self.good_under(i,j)):
			under = self.dp[i-1][j];
		else:
			under = 0;
		if(self.good_left(i,j)):
			left = self.dp[i][j-1];
		else:
			left = 0;
		r = 0;
		if(self.board[i][j] == '1'):
			r = 1;
		self.dp[i][j] = max(under, left)-r; 

	def ans(self):
		X = self.X; Y = self.Y;
		y = 0; x = 0;
		while(y < Y and x < X):
			if(y < Y):
				for i in range(x+1,X):
					self.calc_max(i,y);
				y += 1;
			if(x < X):
				for j in range(y+1,Y):
					self.calc_max(x,j);
				x += 1;
		print(self.dp);
		return self.dp[-1][-1];

for line in stdin:
		T = int(line);
		for t in range(T):
			line = stdin.next();
			s = line.split();
			X = int(s[0]); Y = int(s[1]);
			M = int(s[2]);
			board = [];
			for x in range(X):
				board.append(stdin.next());
			sol = Solver(X,Y,M,board);
			ans = sol.ans();
			if(ans == 0):
				print('Impossible');
			else:
				print(ans);

