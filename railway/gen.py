from random import randint

n = int(1e5)
k = int(1e5)
msg_types = ['blocked', 'opened', 'status']

status = n*[0]

def print_msg():
    i = randint(0, n-1)
    msg_type = msg_types[randint(0, len(msg_types)-1)]

    if (msg_type == 'blocked' and status[i]) or (msg_type == 'opened' and not status[i]):
        print_msg()
    else:
        print i, msg_type

print n

for i in xrange(k):
    print_msg()
