#include <iostream>

using namespace std;

bool remove_city(char* city, int* letters, int& letters_left);
bool recurse(int start, char** cities, int* letters, int city_count, int& letters_left);

int main() {

    char* cities[56] = {(char*)"LOSANGELES", (char*)"CHICAGO", (char*)"HOUSTON", (char*)"PHILADELPHIA", (char*)"SANANTONIO", (char*)"SANDIEGO", (char*)"DALLAS", (char*)"SANJOSE", (char*)"JACKSONVILLE", (char*)"INDIANAPOLIS",
                        (char*)"SANFRANCISCO", (char*)"AUSTIN", (char*)"COLUMBUS", (char*)"FORTWORTH", (char*)"CHARLOTTE", (char*)"DETROIT", (char*)"ELPASO", (char*)"BALTIMORE", (char*)"BOSTON", (char*)"SEATTLE",
                        (char*)"WASHINGTON", (char*)"NASHVILLE", (char*)"DENVER", (char*)"LOUISVILLE", (char*)"MILWAUKEE", (char*)"PORTLAND", (char*)"LASVEGAS", (char*)"OKLAHOMACITY", (char*)"TUCSON", (char*)"FRESNO",
                        (char*)"SACRAMENTO", (char*)"LONGBEACH", (char*)"KANSASCITY", (char*)"MESA", (char*)"VIRGINIABEACH", (char*)"ATLANTA", (char*)"COLORADOSPRINGS", (char*)"OMAHA", (char*)"RALEIGH", (char*)"CLEVELAND",
                        (char*)"TULSA", (char*)"OAKLAND", (char*)"MINNEAPOLIS", (char*)"WICHITA", (char*)"ARLINGTON", (char*)"BAKERSFIELD", (char*)"NEWORLEANS", (char*)"HONOLULU", (char*)"ANAHEIM", (char*)"TAMPA",
                        (char*)"AURORA", (char*)"SANTAANA", (char*)"STLOUIS", (char*)"PITTSBURGH", (char*)"CORPUSCHRISTI", (char*)"RIVERSIDE"};
    int letters[26] = {20, 3, 7, 8, 15, 2, 4, 7, 18, 1, 3, 19, 1, 7, 12, 6, 0, 14, 17, 11, 4, 6, 2, 0, 1, 0};
    int letters_left = 188;

    if (recurse(0, cities, letters, 0, letters_left))
        cout << "\n\nHappy!" << endl;
    else   
        cout << "\n\nSad." << endl;

    return 0;
}

// remove the letters of a city from the list, returning false for fail
bool remove_city(char* city, int* letters, int& letters_left) {
    for (int i = 0; city[i] != '\0'; i++) {
        letters[city[i] - 'A']--;
        letters_left--;
        
        //failed, add previous letters back
        if (letters[city[i] - 'A'] < 0) {
            for (int j = i; j > -1; j--) {
                letters[city[j] - 'A']++;
                letters_left++;
            }
            return false;
        }
    }
    return true;
}

//
bool recurse(int start, char** cities, int* letters, int city_count, int& letters_left) {
    if (city_count > 20) //only 20 cities
        return false;
    
    for (int i = start; i < 56; i++) {
        if (start < 5) //to check progress
            cout << start << ": " << cities[i] << endl;

        //remove the city, see if it works
        if (remove_city(cities[i], letters, letters_left)) {
            if (letters_left == 0) { //success! used all letters
                cout << cities[i] << " ";
                return true;
            }

            if (recurse(i+1, cities, letters, city_count+1, letters_left)) { //recursively call checking all the cities forward, if get "true" then it was a success
                cout << cities[i] << " ";
                return true;
            }
            else { //path was a failure, add letters back
                for (int j = 0; cities[i][j] != '\0'; j++) {
                    letters[cities[i][j] - 'A']++;
                    letters_left++;
                }
            }
        }
    }
    return false;
}