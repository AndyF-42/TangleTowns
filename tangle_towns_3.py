"""
cities = ["Los Angeles", "Chicago", "Houston", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose",
          "Jacksonville", "Indianapolis", "San Francisco", "Austin", "Columbus", "Fort Worth", "Charlotte", "Detroit", "El Paso",
          "Baltimore", "Boston", "Seattle", "Washington", "Nashville", "Denver", "Louisville", "Milwaukee", "Portland", "Las Vegas",
          "Oklahoma City", "Tucson", "Fresno", "Sacramento", "Long Beach", "Kansas City", "Mesa", "Virginia Beach", "Atlanta",
          "Colorado Springs", "Omaha", "Raleigh", "Cleveland", "Tulsa", "Oakland", "Minneapolis", "Wichita", "Arlington",
          "Bakersfield", "New Orleans", "Honolulu", "Anaheim", "Tampa", "Aurora", "Santa Ana", "St. Louis", "Pittsburgh", "Corpus Christi", "Riverside"]
cities = [i.upper().replace(" ", "").replace(".", "") for i in cities]
"""


"""
ALGORITHM
---------
for every city:
    func(cities, letters, city):

func (cities, letters, city):
    make copy of letters
    remove city's letters from copy
    clean_cities(cities, copy)
    for every city:
        func(cities, copy, city)
"""

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

# removes the cities that cannot be made
def clean_cities(cities, letters):
    to_remove = []
    for city in cities:
        temp_letters = letters.copy()
        for letter in city:
            if letter in temp_letters:
                temp_letters.remove(letter)
            else:
                to_remove.append(city)
                break

    cities = [city for city in cities if city not in to_remove]
    return len(to_remove)


def brute_force(cities, letters, city, depth):
    copy_letters = letters.copy() # make a copy of the letters and cities
    copy_cities = cities.copy()

    for letter in city: # remove the letters from the city
        if letter in copy_letters:
            copy_letters.remove(letter)
        else:

            return False # removal failed: return false
    copy_cities.remove(city)

    if depth == 20:
        if not letters:
            print(city)
            return True
        return False
    
    for next_city in copy_cities:
        temp_letters = copy_letters.copy()
        success = brute_force(copy_cities, temp_letters, next_city, depth + 1)
        if success:
            print(city)
            return True
    return False
    
"""
full_cities = cities.copy()
for city in full_cities:
    success = brute_force(cities, letters, city, 1)
    if not success:
        print("NOT " + city)
        cities.remove(city)
    else:
        print("it worked?")
        break
"""

def remove_letters(letters, line):
    for letter in line:
        if letter == ',' or letter == ' ' or letter == '\n':
            continue
        letter = letter.upper()
        if letters[letter] == 0:
            return False
        else:
            letters[letter] -= 1
    return True

def check_done(dict):
    return all(value == 0 for value in dict.values())



letters_dict = {'A': 20, 'B': 3, 'C': 7, 'D': 8, 'E': 15, 'F': 2, 'G': 4, 'H': 7, 'I': 18, 'J': 1, 'K': 3, 'L': 19, 'M': 1,
                'N': 7, 'O': 12, 'P': 6, 'Q': 0, 'R': 14, 'S': 17, 'T': 11, 'U': 4, 'V': 6, 'W': 2, 'X': 0, 'Y': 1, "Z": 0}

file_a = open("new/Tan01.csv", "r")
for line_a in file_a:
    letters_a = letters_dict.copy()
    if not remove_letters(letters_a, line_a):
        print("~(1)~ NOT: " + line_a)
        continue
    
    file_b = open("new/Tan02.csv", "r")
    for line_b in file_b:
        letters_b = letters_a.copy()
        if not remove_letters(letters_b, line_b):
            continue

        file_c = open("new/Tan03.csv", "r")
        for line_c in file_c:
            letters_c = letters_b.copy()
            if not remove_letters(letters_c, line_c):
                continue

            file_d = open("new/Tan04.csv", "r")
            for line_d in file_d:
                letters_d = letters_c.copy()
                if not remove_letters(letters_d, line_d):
                    continue

                file_e = open("new/Tan05.csv", "r")
                for line_e in file_e:
                    letters_e = letters_d.copy()
                    if not remove_letters(letters_e, line_e):
                        continue

                    file_f = open("new/Tan06.csv", "r")
                    for line_f in file_f:
                        letters_f = letters_e.copy()
                        if not remove_letters(letters_f, line_f):
                            continue
                        
                        file_g = open("new/Tan07.csv", "r")
                        for line_g in file_g:
                            letters_g = letters_f.copy()
                            if not remove_letters(letters_g, line_g):
                                continue

                            file_h = open("new/Tan08.csv", "r")
                            for line_h in file_h:
                                letters_h = letters_g.copy()
                                if not remove_letters(letters_h, line_h):
                                    continue

                                file_i = open("new/Tan09.csv", "r")
                                for line_i in file_i:
                                    letters_i = letters_h.copy()
                                    if not remove_letters(letters_i, line_i):
                                        continue

                                    file_j = open("new/Tan10.csv", "r")
                                    for line_j in file_j:
                                        letters_j = letters_i.copy()
                                        if not remove_letters(letters_j, line_j):
                                            continue

                                        file_k = open("new/Tan11.csv", "r")
                                        for line_k in file_k:
                                            letters_k = letters_j.copy()
                                            if not remove_letters(letters_k, line_k):
                                                continue
                                            
                                            file_l = open("new/Tan12.csv", "r")
                                            for line_l in file_l:
                                                letters_l = letters_k.copy()
                                                if not remove_letters(letters_l, line_l):
                                                    continue

                                                file_m = open("new/Tan13.csv", "r")
                                                for line_m in file_m:
                                                    letters_m = letters_l.copy()
                                                    if not remove_letters(letters_m, line_m):
                                                        continue

                                                    file_n = open("new/Tan14.csv", "r")
                                                    for line_n in file_n:
                                                        letters_n = letters_m.copy()
                                                        if not remove_letters(letters_n, line_n):
                                                            continue

                                                        file_o = open("new/Tan15.csv", "r")
                                                        for line_o in file_o:
                                                            letters_o = letters_n.copy()
                                                            if not remove_letters(letters_o, line_o):
                                                                continue

                                                            file_p = open("new/Tan16.csv", "r")
                                                            for line_p in file_p:
                                                                letters_p = letters_o.copy()
                                                                if not remove_letters(letters_p, line_p):
                                                                    continue
                                                                
                                                                file_q = open("new/Tan17.csv", "r")
                                                                for line_q in file_q:
                                                                    letters_q = letters_p.copy()
                                                                    if not remove_letters(letters_q, line_q):
                                                                        continue

                                                                    file_r = open("new/Tan18.csv", "r")
                                                                    for line_r in file_r:
                                                                        letters_r = letters_q.copy()
                                                                        if not remove_letters(letters_r, line_r):
                                                                            continue

                                                                        file_s = open("new/Tan19.csv", "r")
                                                                        for line_s in file_s:
                                                                            letters_s = letters_r.copy()
                                                                            if not remove_letters(letters_s, line_s):
                                                                                continue

                                                                            file_t = open("new/Tan20.csv", "r")
                                                                            for line_t in file_t:
                                                                                letters_t = letters_s.copy()
                                                                                if not remove_letters(letters_t, line_t):
                                                                                    continue

                                                                                if check_done(letters_t):
                                                                                    print("DONE")
                                                                                    print("THIS IS IT:\n" + line_a + line_b + line_c + line_d + line_e)
                                                                                    print(line_f + line_g + line_h + line_i + line_j + line_k + line_l)
                                                                                    print(line_m + line_n + line_o + line_p + line_q + line_r + line_s + line_t)
                                                                                    print(letters_t)
                                                                                    exit()
            print("(3) NOT: " + line_a.strip() + "-" + line_b.strip() + "-" + line_c)
        print("(2) NOT: " + line_a.strip() + "-" + line_b)
    print("(1) NOT: " + line_a)

print("failed")
