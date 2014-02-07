
L = 20;
dist = [18*i for i in range(200)];
price = [(p-100)**2 for p in range(200)];

i = 0;
p = 0;
h = 0;
d = 18;
while(i+1 < len(price)):
	if(i < 100):
		p += 18*price[i];
	else:
		if(i == 100):
			p+=20*price[i];
		elif(i+2 == len(price)):
			p+=16*price[i];
		else:
			p += 18*price[i];
	i+=1;
print p;
