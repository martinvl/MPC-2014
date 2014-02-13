#include <iostream>
#include <cstdint>

uint64_t pow(uint64_t a, uint64_t n, uint64_t p)
{
    if (n == 0) return 1;
    if (n == 1) return a;

    if (n % 2 == 0) {
        return pow((a * a) % p, n/2, p) % p;
    } else  {
        return a * pow((a * a) % p, (n - 1)/2, p) % p;
    }
}

int main(int argc, char* argv[])
{
    uint64_t a, b, n;
    std::cin >> a >> b >> n;

    std::cout << pow(a, b, n) << std::endl;

    return 0;
}
