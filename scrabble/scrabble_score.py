# Scrabble Score

# Write a program that, given a word, computes the scrabble score for that word.
# Letter Values

# You'll need these:

#     1 Letter                           Value
#     2 A, E, I, O, U, L, N, R, S, T       1
#     3 D, G                               2
#     4 B, C, M, P                         3
#     5 F, H, V, W, Y                      4
#     6 K                                  5
#     7 J, X                               8
#     8 Q, Z                               10


# Examples

#       "cabbage" should be scored as worth 14 points:

#           3 points for C
#           1 point for A, twice
#           3 points for B, twice
#           2 points for G
#           1 point for E

#       And to total:

#           3 + 2*1 + 2*3 + 2 + 1
#           = 3 + 2 + 6 + 3
#           = 5 + 9
#           = 14

def score(word):
    total = 0

    lists1 = {

        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10

    }

    for i in word.upper():
        if i == '\t' or i == '\n':
            total += 0
        elif type(i) == int:
            total = 0
            break
        elif i == " ":
            total = 0
            break
        elif i in '0123456789':
            total = 0
            break
        else:
            total += lists1[i]

    return total
