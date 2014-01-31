class Solver:

	def __init__(self):
		self.dist = [0];
		self.price = [0];
		self.L = 0;

	def solve(self, dist, price, L):
		self.dist = dist; self.price = price; self.L = L;
		return self.solve();

	#dynamic programming solution.
	#dp[i][l] is the optimal cost function
	#when arriving at city i with l fuel in the tank.
	#
	#Complexity:
	#O(N*L^2)
	#
	#Exists better dp performance??
	def solve(self):
		dist = self.dist; price = self.price; L = self.L;
		
		dp = [[2**30 for l in range(L+1)] for i in range(len(dist))];
		self.dp = dp;

		i = 1;
		dp[0][0] = 0;
		for i in range(1,len(dp)):
			for l in range(len(dp[i])):
				k = 1;
				while(i-k>=0):
 					d = dist[i]-dist[i-k]; 
					if(d > L-l):
						break;
					for b in range(len(dp[i])):
						if(0<=l+d-b and l+d-b <= L):
							dp[i][l] = min(dp[i][l],
									dp[i-k][l+d-b]+b*price[i-k]);
					k+=1;
		return dp[-1][0];

	def ans(self, dist, price, L):
		self.dist = dist; self.price = price; self.L = L;
		a = self.solve();
		if(a >= 2**30):
			return "Stay home";
		return str(a);


sol = Solver();

#Case 1
dist1 = [0, 3];
price1 = [100, 0];
L1=2;   

print(sol.ans(dist1, price1, L1));

#Case 2
dist2 = [0,4, 6, 8, 18, 28];
price2 = [6,3,9,5,2,0];
L2 = 10;

print(sol.ans(dist2, price2, L2));

