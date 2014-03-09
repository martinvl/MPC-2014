from sys import stdin
from sets import Set

# This is an attempt to create an alternative solution, that do not
# require implementation of SAT. However, due to poor programming
# skills in python (and sloppy coding), it may very well be wrong.

def get_possible_trucks(city):
    if city == 'Kristiansand':
        return (0, 2)
    elif city == 'Bergen':
        return (0, 1)
    elif city == 'Trondheim':
        return (1, 2)

# Add currentPackage to the setup using a given truck. Must not
# conflict with decidedPackages, and must be compatible with
# requirements in packageMap. Returns a boolean indicating success
def fill(truck, currentPackage, decidedPackages, packageMap):
    decidedPackages[currentPackage] = truck
    dest, incompabilities = packageMap[currentPackage]
#    print truck, currentPackage, decidedPackages, packageMap
    for incompability in incompabilities:
        if (incompability in decidedPackages):
            if (truck == decidedPackages[incompability]):
                return False
            continue
        newdest, blah = packageMap[incompability]
        truckA, truckB = get_possible_trucks(newdest)
        if (truck == truckA):
            if (fill(truckB, incompability, decidedPackages, packageMap)):
                continue
        if (truck == truckB):
            if (not fill(truckA, incompability, decidedPackages, packageMap)):
                return False
        continue
    return True

n = int(stdin.readline())
packageMap = {}
for package, destination, line in zip(xrange(n), stdin.readline().split(), stdin):
    packageMap[package] = (destination, map(int, line.split()))
tobedelivered = Set(xrange(n))
while (tobedelivered):
    elem = tobedelivered.pop()
    dest, line = packageMap[elem]
    truckA, truckB = get_possible_trucks(dest)
    decidedPackages = {}
    if (not fill(truckA, elem, decidedPackages, packageMap)):
        if (not fill(truckB, elem, decidedPackages, packageMap)):
            print "Impossible"
            break
if (not tobedelivered):
    print "Possible"
