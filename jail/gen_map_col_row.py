from sys import stdin;
#Takes a given input file, and puts an upper row
#and a right column of only zeros. Dimensions of
#the new map are both one larger

l = stdin.readline().split();
M = int(l[0])+1; N = int(l[1])+1;
I = int(l[2]);
print(''+str(M) + ' '+str(N)+' '+str(I));

def line_of_zeros(K):
	l = '';
	for k in range(K):
		l += '0';
		if(k < K-1):
			l += ' ';
	print(l);

def add_zero_to_end(line):
	line = line.strip();
	line += ' 0';
	print(line);

line_of_zeros(M-1);

for n in range(N-1):
	l = stdin.next();
	add_zero_to_end(l);

line_of_zeros(M);

for n in range(N-2):
	l = stdin.next();
	add_zero_to_end(l);
