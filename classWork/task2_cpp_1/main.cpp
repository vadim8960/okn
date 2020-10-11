#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

int main() {
    std::string s1;
    std::string s2;
    std::cout << "S1: ";
    std::cin >> s1;
    std::cout << "S2: ";
    std::cin >> s2;

    std::string s = s1;

    s.erase( std::remove_if( s.begin(), s.end(), [&s](auto & el) -> bool { static int i = 0; return !(i++ % 2); }), s.end());
    int n = std::distance(s.begin(), std::find_end(s.begin(), s.end(), s2.begin(), s2.end()));

    std::cout << n << std::endl;
    return 0;
}
