#include <iostream>
#include <string>

int main() {
    std::string s1 = "abchelloabcworld";
    std::string s2 = "abc";
    int count = 0, pos = s1.find(s2, 0);
    while (pos != std::string::npos) {
        ++count;
        pos = s1.find(s2, pos + s2.size());
    }
    std::cout << count << std::endl;
    return 0;
}
