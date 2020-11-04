#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

void MxV(const double * A, const double * b, unsigned rows, unsigned cols, double * r)  // r = A * b
{const double * pb, * pbfin = b + cols, * rfin = r + rows;
    for(; r != rfin; r++)
    {*r = 0;
        pb = b;
        for(; pb != pbfin; pb++, A++)
            *r += *A * *b;
    }
}

void MxM(const double * A, const double * B, unsigned rows, unsigned cols, unsigned cols2, double * С)
{
    double * Bcopy = (double *)malloc(sizeof(double) * cols2 * cols );
    for (int i = 0; i < cols; ++i)
        for (int j = 0; j < cols2; ++j)
            *(Bcopy + j * cols2 + i) = *(B + i * cols + j);

    const double * Bend = Bcopy + cols * cols2 + 1;
    for (; Bcopy != Bend; Bcopy += cols2, С += cols2) {
        MxV(A, Bcopy, rows, cols, С);
    }

    free(Bcopy);
}


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
