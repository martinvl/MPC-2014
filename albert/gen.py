from sys import stdin;

def form_print(dist, price, L):
	print(L);
	print(len(dist));
	for i in range(len(dist)):
		print '%i %i' % (dist[i], price[i])

#T1
#Ans calculated analytic: 500499
L = 1;
dist = [i for i in range(1000)];
price = [1000-i for i in dist];

form_print(dist, price, L);

#T2
#Ans calculated analytic: 498501
price = [i for i in range(1000)];

form_print(dist,price,L);

#T3
#Ans = 500499
L = 20;
dist = [i for i in range(1000)];
price = [1000-i for i in dist];

form_print(dist, price, L)

#T4
#Ans = 11804974, see programs

L = 20;
dist = [18*i for i in range(200)];
price = [((p-100)**2) for p in range(200)];

form_print(dist, price, L);


