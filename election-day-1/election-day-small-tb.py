# @EXPECTED_RESULTS@: TIMELIMIT

#N log(N) solution (simulation)

elim = [False];


class Solver:

	def __init__(self):
		self.elim = [False];

	def get_next_next(self, i):
		elim = self.elim;
		N = len(elim);
		j=i;
		one = False;
		while(True):
			j=j+1; j=j% N;
			if(not one and j==i):
				return -1;
			elif(not one and not elim[j]):
				one = True;
			elif(one and not elim[j]):
				return j;

	def solve_iter(self,N):
		self.elim = N*[False];
		elim = self.elim;
		if(N==1):
			return 1;
		i = 1;
		while(True):
			j = self.get_next_next(i);
			if(j==-1):
				return i+1;
			elim[i] = True;
			i = j;


sol = Solver(); 
N=100000;
it = 1;
i = 0;
while(i<it):
	s = sol.solve_iter(N);
	i+=1;
print(s);

