# @EXPECTED_RESULTS@: CORRECT

#Analytical solution
import math;

elim = [False];


class Solver:

	def __init__(self):
		self.elim = [False];

	def solve_const(self,N):
		p = int(math.floor(math.log(N, 2)));
		l = N % 2**p;
		return 2*l+1;

it = 20000;
N = 1000000000000000000000000000000;
i=0;
sol = Solver();
while(i<it):
	i+=1;
	s=sol.solve_const(N);
print s;

