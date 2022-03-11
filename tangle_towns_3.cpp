#include <iostream>
#include <string>


/*
IDEA
----

bool remove_city(& city, char*& letters, int& used_letters):
    for every letter in city:
        if in letters: remove from letters (change to .)
                        increase used_letters
        else: return false
    return true


bool func(int start, const string[] cities, char[]   &    letters)
    for i=start to i=cities_length
        remove the letters from letters
        if fail -> ??
        func(i+1, cities, letters)
        add the letters back


remove city1
    remove city2
        remove city3 -- FAIL
        add city3
        remove city4 -- FAIL
        add city4
        remove city5 -- FAIL
        add city5
        (only 5 cities)
    add city2
    remove city3
        remove city4 -- FAIL
        add city4
        remove 5...
    add city3
    remove city4 -- FAIL
    add city4
add city1
remove city2
    remove city5
        all letters gone? yes -- DONE

*/

using namespace std;

int main() {
    //might be able to change to const char[]
    char* cities[56] = {(char*)"LOSANGELES", (char*)"CHICAGO", (char*)"HOUSTON", (char*)"PHILADELPHIA", (char*)"SANANTONIO", (char*)"SANDIEGO", (char*)"DALLAS", (char*)"SANJOSE", (char*)"JACKSONVILLE", (char*)"INDIANAPOLIS",
                        (char*)"SANFRANCISCO", (char*)"AUSTIN", (char*)"COLUMBUS", (char*)"FORTWORTH", (char*)"CHARLOTTE", (char*)"DETROIT", (char*)"ELPASO", (char*)"BALTIMORE", (char*)"BOSTON", (char*)"SEATTLE",
                        (char*)"WASHINGTON", (char*)"NASHVILLE", (char*)"DENVER", (char*)"LOUISVILLE", (char*)"MILWAUKEE", (char*)"PORTLAND", (char*)"LASVEGAS", (char*)"OKLAHOMACITY", (char*)"TUCSON", (char*)"FRESNO",
                        (char*)"SACRAMENTO", (char*)"LONGBEACH", (char*)"KANSASCITY", (char*)"MESA", (char*)"VIRGINIABEACH", (char*)"ATLANTA", (char*)"COLORADOSPRINGS", (char*)"OMAHA", (char*)"RALEIGH", (char*)"CLEVELAND",
                        (char*)"TULSA", (char*)"OAKLAND", (char*)"MINNEAPOLIS", (char*)"WICHITA", (char*)"ARLINGTON", (char*)"BAKERSFIELD", (char*)"NEWORLEANS", (char*)"HONOLULU", (char*)"ANAHEIM", (char*)"TAMPA",
                        (char*)"AURORA", (char*)"SANTAANA", (char*)"STLOUIS", (char*)"PITTSBURGH", (char*)"CORPUSCHRISTI", (char*)"RIVERSIDE"};

    char letters[188] = {'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
                         'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'E', 'E',
                         'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'G', 'H',
                         'H', 'H', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
                         'I', 'I', 'I', 'I', 'J', 'K', 'K', 'K', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L',
                         'L', 'L', 'L', 'L', 'L', 'L', 'L', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O',
                         'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'P', 'P', 'P', 'P', 'R', 'R', 'R', 'R', 'R', 'R', 'R',
                         'R', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
                         'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V',
                         'V', 'V', 'V', 'V', 'V', 'W', 'W', 'Y'};
    
    int used_letters = 0;

    for (int i = 0; i < 56; i++) {
        cout << cities[i] << endl;
    }

    return 0;
}