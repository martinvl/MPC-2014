import sys

M = int(sys.argv[1]);
N = int(sys.argv[2]);
I = int(sys.argv[3]);

print('' + str(M) + ' '+str(N) + ' '+str(I));

def printzeros(K):
	l = '';
	for k in range(K):
		l += '0';
		if(k < K-1):
			l+= ' ';
	print(l);

for n in range(N):
	printzeros(M-1);
for n in range(N-1):
	printzeros(M);

