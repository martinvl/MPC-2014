from sys import stdin;
import numpy as np;

a = np.array([[0 for k in range(5)] for i in range(5)]);

print(a);




for line in stdin:
		T = int(line);
		for t in range(T):
			line = stdin.next();
			s = line.split();
			X = int(s[0]); Y = int(s[1]);
			M = int(s[2]);
			res = solver(X,Y,M);




