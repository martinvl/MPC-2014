from sys import argv, exit
from random import randint

if len(argv) < 3:
    print 'USAGE: %s <test.in> <jury.out>' % argv[0]
    exit(1)

test_in = open(argv[1], 'w')
jury_out = open(argv[2], 'w')

R = 'Rock'
P = 'Paper'
S = 'Scissors'

first_moves = [R, P, S]
second_moves = {R:[P, S], P:[R, S], S:[R, P]}
f = len(first_moves)
s = len(second_moves[R])

T = 10
N = int(1e4)

test_in.write('%d\n' % T)

for i in xrange(T):
    for j in xrange(N):
        you_first = first_moves[randint(0, f-1)]
        friend_first = first_moves[randint(0, f-1)]
        friend_second = second_moves[friend_first][randint(0, s-1)]

        test_in.write('%s %s\n' % (you_first, friend_first))
        jury_out.write('%s\n' % friend_second)

test_in.close()
jury_out.close()
