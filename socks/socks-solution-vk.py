# @EXPECTED_RESULTS@: CORRECT

from sys import stdin

N = int(stdin.readline())
frequency = {}
for test_case in range(N):
    label = stdin.readline().strip()
    if label in frequency.keys():
        frequency[label] += 1
    else:
        frequency[label] = 1

socksess = True
removeList = []
for label in frequency.keys():
    if frequency[label] == 1:
        removeList.append(label)
        socksess = False

if socksess:
    print "Sock-sess"
else:
    removeList.sort()
    for label in removeList:
        print label





