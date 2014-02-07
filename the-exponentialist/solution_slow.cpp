#include <iostream>
#include <cstdint>

int main()
{
    uint64_t a, b, n;
    std::cin >> a >> b >> n;

    uint64_t res = 1;
    for (int i = 0; i < b; ++i) {
        res = (res * a) % n;
    }

    std::cout << res << std::endl;

    return 0;
}
