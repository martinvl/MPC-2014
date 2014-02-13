from sys import stdin

n = int(stdin.readline())

for line in stdin:
    print 'Reject' if line.strip() == 'Complaint' else 'Investigate'
