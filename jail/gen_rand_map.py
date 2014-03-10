import sys;
import random;

M = int(sys.argv[1].strip());
N = int(sys.argv[2].strip());
I = int(sys.argv[3].strip());

dim = ''+ str(M) + ' ' + str(N) + ' ' + str(I)
print(dim);
b = ' ';
for n in range(N):
	line = '';
	for m in range(M-1):
		line += str(random.randint(0,1));
		if(m == M-2):
			print(line);
		line += b;

for n in range(N-1):
	line = '';
	for m in range(M):
		line += str(random.randint(0,1));
		if(m == M-1):
			print(line);
		line += b;
