from sys import stdin

def pow(a, n, p):
    if n == 0: return 1
    if n == 1: return a

    if n % 2 == 0: return pow(a**2 % p, n / 2, p) % p
    else:          return a * pow(a**2 % p, (n - 1)/2, p) % p

if __name__ == "__main__":
    print(pow(*map(int, stdin.readline().split())))
