cities = ["New York City", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Phoenix", "San Antonio", "San Diego", "Dallas", "San Jose", "Jacksonville", "Indianapolis", "San Francisco", "Austin", "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso", "Memphis", "Baltimore", "Boston", "Seattle", "Washington", "Nashville", "Denver", "Louisville", "Milwaukee", "Portland", "Las Vegas", "Oklahoma City", "Albuquerque", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa", "Virginia Beach", "Atlanta", "Colorado Springs", "Omaha", "Raleigh", "Miami", "Cleveland", "Tulsa", "Oakland", "Minneapolis", "Wichita", "Arlington", "Bakersfield", "New Orleans", "Honolulu", "Anaheim", "Tampa", "Aurora", "Santa Ana", "St. Louis", "Pittsburgh", "Corpus Christi", "Riverside"]
cities = [i.upper().replace(" ", "").replace(".", "") for i in cities]

""" FIX LETTERS
letters = "A(20), B(3), C(7), D(8), E(15), F(2), G(4), H(7), I(18), J(1), K(3), L(19), M(1), N(7), O(12), P(6), Q(0), R(14), S(17), T(11), U(4), V(6), W(2), X(0), Y(1), Z(0)"
letters = letters.split(", ")
new_letters = []
for i, letter in enumerate(letters):
    letters[i] = letter.split("(")
    for j in range(int(letters[i][1][:-1])):
        new_letters.append(letters[i][0])
print(new_letters)
"""
letters = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
           'B', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'E', 'E',
           'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G', 'G', 'H',
           'H', 'H', 'H', 'H', 'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
           'I', 'I', 'I', 'I', 'J', 'K', 'K', 'K', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L',
           'L', 'L', 'L', 'L', 'L', 'L', 'L', 'M', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O',
           'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'P', 'P', 'P', 'P', 'R', 'R', 'R', 'R', 'R', 'R', 'R',
           'R', 'R', 'R', 'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S',
           'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V',
           'V', 'V', 'V', 'V', 'V', 'W', 'W', 'Y']

def clean_cities(cities, letters):
    temp = letters.copy()
    to_remove = []
    for city in cities:
        for letter in city:
            if letter in letters:
                letters.remove(letter)
            else:
                to_remove.append(city)
                #print(city, letter)
                break
        letters = temp.copy()

    for city in to_remove:
        cities.remove(city)
    return len(to_remove)


def brute_force(cities, letters, depth):
    

clean_cities(cities, letters)
brute_force(cities, letters, 0)