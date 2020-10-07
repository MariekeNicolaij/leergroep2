# Voorbeeldopgave lists, resultaat: [2, 7, 5, 9]

e = [2, 7, 1]
pi = [3, 1, 4, 1, 5, 9]

# Lijsten maken en bewerken

answer0 = e[0:2] + pi[-2:]
print("answer0: ", answer0)

answer1 = e[1:]
print("answer1: ", answer1)

answer2 = e[2:3] + pi[1:2] + e[:1]
print("answer2: ", answer2)

answer3 = pi[1:]
print("answer3: ", answer3)

answer4 = e[::-2] + pi[::2]
print("answer4: ", answer4)

# Strings slicen en indexeren

print()

h = "hanze"
s = "hogeschool"
g = "groningen"

answer5 = s[0:2] + g[4]
print("answer5: ", answer5)

# 3 bewerkingen 😎
answer6 = s[4:8] + g[7:] + g[7:]
print("answer6: ", "mooie " + answer6)

answer7 = h[1:] + s[1:]
print("answer7: ", answer7)

answer8part1 = g[::-1][2:4] + h[1:2]
answer8part2 = h[0:2]
answer8 = answer8part1 * 2 + answer8part2 *  5
print("answer8: ", answer8)

answer9part1 = s[::-1][6:9]
answer9part2 = g[::-1][5:7]
answer9 = s[-1::] + answer9part1 + answer9part2 + answer9part1
print("answer9: ", answer9)

answer10 = s[-1::] + g[::-1][1:3] + g[0:1] + g[4:7] + s[4:5]
print("answer10: ", answer10)
