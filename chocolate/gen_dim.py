import sys
import random

dim_upper = int(sys.argv[1]);

R = random.randint(1, dim_upper);
C = random.randint(1, dim_upper);

print('' + str(R)+ ' ' +str(C));
