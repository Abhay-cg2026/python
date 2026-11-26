# # Q1. Number Pair Generator - print all (i, j) pairs from 1 to 3
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)


# # Q2. Multiplication Pair - print i x j = result for every pair 1..N
# n = 3
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(f"{i} x {j} = {i * j}")


# # Q3. Repeated Character Grid - character rectangle of given rows/columns
# ch, rows, cols = "*", 3, 4
# for i in range(rows):
#     line = ""
#     for j in range(cols):
#         line += ch
#     print(line)


# # Q4. Coordinate Grid - print every (row,col) coordinate
# rows, cols = 2, 3
# for i in range(rows):
#     line = ""
#     for j in range(cols):
#         line += f"({i},{j}) "
#     print(line.strip())


# # Q5. Row Number Pattern - row number repeated N times in each row
# n = 4
# for i in range(1, n + 1):
#     line = ""
#     for j in range(n):
#         line += str(i)
#     print(line)


# # Q6. Column Number Pattern - 1..N in every row
# n = 4
# for i in range(n):
#     line = ""
#     for j in range(1, n + 1):
#         line += str(j)
#     print(line)


# # Q7. Increasing Number Grid - 1, 12, 123, ...
# n = 4
# for i in range(1, n + 1):
#     line = ""
#     for j in range(1, i + 1):
#         line += str(j)
#     print(line)


# # Q8. Decreasing Number Grid - 1..N, then one fewer each row
# n = 4
# for i in range(n, 0, -1):
#     line = ""
#     for j in range(1, i + 1):
#         line += str(j)
#     print(line)


# # Q9. Star Rectangle - rows x columns of *
# rows, cols = 3, 5
# for i in range(rows):
#     line = ""
#     for j in range(cols):
#         line += "*"
#     print(line)


# # Q10. Alternating 0 and 1 - N x N grid, columns alternate 0/1
# n = 4
# for i in range(n):
#     line = ""
#     for j in range(n):
#         line += str(j % 2)
#     print(line)


# # Q11. Even Number Grid - only even column values in each row
# rows, cols = 3, 6
# for i in range(rows):
#     line = []
#     for j in range(1, cols + 1):
#         if j % 2 == 0:
#             line.append(str(j))
#     print(" ".join(line))


# # Q12. Odd Number Grid - odd numbers 1..N in every row (N rows)
# n = 7
# for i in range(n):
#     line = []
#     for j in range(1, n + 1):
#         if j % 2 != 0:
#             line.append(str(j))
#     print(" ".join(line))


# # Q13. Even-Odd Classification - E if i+j even else O (1..4)
# for i in range(1, 5):
#     line = []
#     for j in range(1, 5):
#         line.append("E" if (i + j) % 2 == 0 else "O")
#     print(" ".join(line))


# # Q14. Equal Coordinate Detector - Same if i==j else Different
# n = 3
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, n + 1):
#         line.append("Same" if i == j else "Different")
#     print(" ".join(line))


# # Q15. Diagonal Values - 1 on main diagonal, 0 elsewhere
# n = 4
# for i in range(n):
#     line = []
#     for j in range(n):
#         line.append("1" if i == j else "0")
#     print(" ".join(line))


# # Q16. Number Divisibility Grid - X if i divisible by j else -
# for i in range(1, 6):
#     line = []
#     for j in range(1, 6):
#         line.append("X" if i % j == 0 else "-")
#     print(" ".join(line))


# # Q17. Multiples Detector - for each i print j (1..N) that are multiples of i
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, n + 1):
#         if j % i == 0:
#             line.append(str(j))
#     print(" ".join(line))


# # Q18. Pair Sum Filter - pairs from 1..N whose sum > N
# n = 4
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j > n:
#             print(i, j)


# # Q19. Pair Product Filter - print pair and product only when product is even
# n = 3
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if (i * j) % 2 == 0:
#             print(i, j, i * j)


# # Q20. Special Coordinate - SPECIAL (i==j) has priority over PAIR (i+j==N), else NORMAL
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, n + 1):
#         if i == j:
#             line.append("SPECIAL")
#         elif i + j == n:
#             line.append("PAIR")
#         else:
#             line.append("NORMAL")
#     print(" ".join(line))


# # Q21. Character Repetition - each character printed three times
# s = "CAT"
# for ch in s:
#     line = ""
#     for k in range(3):
#         line += ch
#     print(line)


# # Q22. Character with Position - each char with repetition numbers 0,1,2
# s = "AB"
# for ch in s:
#     for k in range(3):
#         print(ch, k)


# # Q23. Compare Every Character - every ordered pair labelled Same/Different
# s = "AB"
# for a in s:
#     for b in s:
#         print(f"{a}/{b} is", "Same" if a == b else "Different")


# # Q24. Character Matching - print equal character pairs of two strings
# s1, s2 = "ABC", "BCD"
# for a in s1:
#     for b in s2:
#         if a == b:
#             print(a, b)


# # Q25. Count Matching Characters - count equal comparisons (no count())
# s1, s2 = "ABC", "BCD"
# total = 0
# for a in s1:
#     for b in s2:
#         if a == b:
#             total += 1
# print(total)


# # Q26. Character Frequency Without count() - occurrences via nested loops
# s = "BANANA"
# for i in range(len(s)):
#     seen_before = False
#     for k in range(i):
#         if s[k] == s[i]:
#             seen_before = True
#     if seen_before:
#         continue
#     f = 0
#     for j in range(len(s)):
#         if s[j] == s[i]:
#             f += 1
#     print(f"{s[i]} = {f}")


# # Q27. Vowel-Consonant Classification - compare against "AEIOUaeiou"
# s = "AbC"
# vowels = "AEIOUaeiou"
# for ch in s:
#     kind = "Consonant"
#     for v in vowels:
#         if ch == v:
#             kind = "Vowel"
#     print(f"{ch} = {kind}")


# # Q28. Common Characters - characters in both strings (no set())
# s1, s2 = "HELLO", "WORLD"
# result = ""
# for a in s1:
#     for b in s2:
#         if a == b:
#             already = False
#             for r in result:
#                 if r == a:
#                     already = True
#             if not already:
#                 result += a
# print("Common characters:", " ".join(result))


# # Q29. Character Pair Generator - every ordered pair of characters
# s = "ABC"
# for a in s:
#     for b in s:
#         print(a, b)


# # Q30. Different Character Pairs - ordered pairs with different positions
# s = "ABC"
# for i in range(len(s)):
#     for j in range(len(s)):
#         if i != j:
#             print(s[i], s[j])


# # Q31. Same or Different Pair - each pair with Same/Different label
# s = "AAB"
# for a in s:
#     for b in s:
#         print(a, b, "Same" if a == b else "Different")


# # Q32. Vowel-Consonant Pair - first is vowel, second is consonant
# s = "ABEC"
# vowels = "AEIOUaeiou"
# for a in s:
#     for b in s:
#         a_vowel = False
#         b_vowel = False
#         for v in vowels:
#             if a == v:
#                 a_vowel = True
#             if b == v:
#                 b_vowel = True
#         if a_vowel and not b_vowel:
#             print(f"{a}-{b}")


# # Q33. Same Case Pair - pairs (different positions) with same case
# s = "AbCD"
# for i in range(len(s)):
#     for j in range(len(s)):
#         if i != j:
#             a, b = s[i], s[j]
#             if (a.isupper() and b.isupper()) or (a.islower() and b.islower()):
#                 print(a, b)


# # Q34. ASCII Difference - pair and absolute ASCII difference
# s = "ABC"
# for i in range(len(s)):
#     for j in range(len(s)):
#         if i != j:
#             d = ord(s[i]) - ord(s[j])
#             if d < 0:
#                 d = -d
#             print(f"{s[i]} {s[j]} -> {d}")


# # Q35. ASCII Relationship - Increasing / Decreasing / Same by ASCII value
# s = "ABC"
# for a in s:
#     for b in s:
#         if ord(a) < ord(b):
#             r = "Increasing"
#         elif ord(a) > ord(b):
#             r = "Decreasing"
#         else:
#             r = "Same"
#         print(f"{a}->{b} {r}")


# # Q36 - Q42: skipped (Level 5, split() problems)


# # Q43. Growing Inner Loop - for each i, inner loop 1..i
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, i + 1):
#         line.append(str(j))
#     print(" ".join(line))


# # Q44. Shrinking Inner Loop - inner size decreases every row
# n = 4
# for i in range(n, 0, -1):
#     line = []
#     for j in range(1, i + 1):
#         line.append(str(j))
#     print(" ".join(line))


# # Q45. Multiplication Triangle - row i prints i*1 .. i*i
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, i + 1):
#         line.append(str(i * j))
#     print(" ".join(line))


# # Q46. Conditional Dynamic Loop - inner loop i times, print only even inner values
# # (Rows with no even value are skipped; sample output in the sheet looks inconsistent with the rule.)
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, i + 1):
#         if j % 2 == 0:
#             line.append(str(j))
#     if line:
#         print(" ".join(line))


# # Q47. Dynamic Range Based on Input - i = 0..N-1, inner range(i)
# n = 4
# for i in range(n):
#     line = []
#     for j in range(i):
#         line.append(str(j))
#     if line:
#         print(" ".join(line))


# # Q48. Reverse Dynamic Range - for each i print i down to 1
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(i, 0,-1):
#         line.append(str(j))
#     print(" ".join(line))


# # Q49. Factors of Every Number - factors of each number 1..N
# n = 6
# for i in range(1, n + 1):
#     f = []
#     for j in range(1, i + 1):
#         if i % j == 0:
#             f.append(str(j))
#     print(i, "->", " ".join(f))


# # Q50. Perfect Number Detector - perfect numbers up to N via divisor sums
# n = 30
# res=[]
# for i in range(1, n + 1):
#     s=0
#     for j in range(1, i):
#         if i % j == 0:
#             s += j
#     if s == i:
#         res.append(str(i))
# print("Perfect:", ", ".join(res))


# # Q51. Prime Numbers Using Nested Loops - primes from 2 to N
# n = 20
# res = []
# for i in range(2, n + 1):
#     prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             prime = False
#             break
#     if prime:
#         res.append(str(i))
# print(" ".join(res))


# # Q52. Prime Factor Display - for every prime up to N show its factors
# n = 10
# for i in range(2, n + 1):
#     prime = True
#     for d in range(2, i):
#         if i % d == 0:
#             prime = False
#             break
#     if prime:
#         f = []
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 f.append(str(j))
#         print(f"{i}->" + ",".join(f))


# # Q53. Common Factors - common factors of A and B
# a, b = 12, 18
# res = []
# for i in range(1, a + 1):
#     for j in range(1, b + 1):
#         if i == j and a % i == 0 and b % j == 0:
#             res.append(str(i))
# print(" ".join(res))


# # Q54. Common Multiples - common multiples of A and B up to a limit
# a, b, limit = 6, 8, 30
# res = []
# for x in range(a, limit + 1, a):
#     for y in range(b, limit + 1, b):
#         if x == y:
#             res.append(str(x))
# print("Common multiples:", " ".join(res))


# # Q55. Pair With Greatest Product - best pair from 1..N
# n = 4
# best, bp = 0, (0, 0)
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i * j > best:
#             best, bp = i * j, (i, j)
# print(f"Pair = {bp[0]},{bp[1]}")
# print(f"Product = {best}")


# # Q56. Pair With Target Sum - pairs 1..N whose sum equals target
# n, target = 5, 7
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i + j == target:
#             print(i, j)


# # Q57. Right Triangle - star triangle
# n = 4
# for i in range(1, n + 1):
#     line = ""
#     for j in range(i):
#         line += "*"
#     print(line)


# # Q58. Number Triangle - 1, 12, 123, ...
# n = 4
# for i in range(1, n + 1):
#     line = ""
#     for j in range(1, i + 1):
#         line += str(j)
#     print(line)


# # Q59. Repeated Number Triangle - row number repeated row times
# n = 4
# for i in range(1, n + 1):
#     line = ""
#     for j in range(i):
#         line += str(i)
#     print(line)


# # Q60. Inverted Triangle - decreasing star rows
# n = 4
# for i in range(n, 0, -1):
#     line = ""
#     for j in range(i):
#         line += "*"
#     print(line)


# # Q61. Right-Aligned Triangle - right aligned stars
# n = 4
# for i in range(1, n + 1):
#     line = ""
#     for j in range(n - i):
#         line += " "
#     for j in range(i):
#         line += "*"
#     print(line)


# # Q62. Number Pyramid - centered 1, 123, 12345, ...
# n = 4
# for i in range(1, n + 1):
#     line = " " * (n - i)
#     for j in range(1, 2 * i):
#         line += str(j)
#     print(line)


# # Q63. Repeated Number Pyramid - centered row number repeated 2i-1 times
# n = 4
# for i in range(1, n + 1):
#     line = " " * (n - i)
#     for j in range(2 * i - 1):
#         line += str(i)
#     print(line)


# # Q64. Inverted Pyramid - inverted centered number pyramid (widths 7,5,3,1)
# n = 4
# for i in range(n, 0, -1):
#     line = " " * (n - i)
#     for j in range(1, 2 * i):
#         line += str(j)
#     print(line)


# # Q65. Diamond Pattern - star diamond
# n = 4
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))


# # Q66. Hollow Rectangle - only the boundary
# rows, cols = 4, 5
# for i in range(rows):
#     line = ""
#     for j in range(cols):
#         if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
#             line += "*"
#         else:
#             line += " "
#     print(line)


# # Q67. Hollow Triangle - hollow right triangle
# n = 5
# for i in range(1, n + 1):
#     line = ""
#     for j in range(1, i + 1):
#         if j == 1 or j == i or i == n:
#             line += "*"
#         else:
#             line += " "
#     print(line)


# # Q68. Number Border Pattern - 1 on border, 0 inside
# n = 5
# for i in range(n):
#     line = ""
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             line += "1"
#         else:
#             line += "0"
#     print(line)


# # Q69. Diagonal Cross - * on both diagonals
# n = 5
# for i in range(n):
#     line = ""
#     for j in range(n):
#         if i == j or i + j == n - 1:
#             line += "*"
#         else:
#             line += " "
#     print(line.rstrip())


# # Q70. Number and Character Grid - word characters combined with column numbers
# word, n = "ABCD", 4
# for ch in word:
#     line = []
#     for j in range(1, n + 1):
#         line.append(f"{ch}{j}")
#     print(" ".join(line))


# # Q71. Character + ASCII Filter - pairs with ASCII difference > 5
# s = "ABCDEF"
# for a in s:
#     for b in s:
#         d = ord(a) - ord(b)
#         if d < 0:
#             d = -d
#         if d > 5:
#             print(a, b, d)


# # Q72. Word Pair Analyzer - lengths and first-character comparison for each pair
# words = "I love code".split()
# for a in words:
#     for b in words:
#         same = "Same" if a[0] == b[0] else "Different"
#         print(f"{a}({len(a)}) {b}({len(b)}) -> First char: {same}")


# # Q73. Student Marks Matrix - marks, total and average of 3 students x 4 subjects
# marks = [[80, 70, 90, 60], [60, 75, 80, 85], [90, 90, 95, 80]]
# for i in range(len(marks)):
#     total = 0
#     for j in range(len(marks[i])):
#         total += marks[i][j]
#     print(f"Student {i + 1}: {marks[i]} Total={total} Average={total / len(marks[i])}")


# # Q74. Multiplication Table Matrix - tables 1..N from x1 to x10
# n = 3
# for i in range(1, n + 1):
#     print(f"Table of {i}")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")


# # Q75. Attendance Checker - count present/absent per student
# att = [["P", "A", "P", "P"], ["A", "P", "A", "P"]]
# for i in range(len(att)):
#     p = a = 0
#     for d in att[i]:
#         if d == "P":
#             p += 1
#         else:
#             a += 1
#     print(f"Student {i + 1} Present={p} Absent={a}")


# # Q76. Mini Seating System - alphabet rows + numeric columns
# rows, cols = 3, 4
# for i in range(rows):
#     line = []
#     for j in range(1, cols + 1):
#         line.append(chr(65 + i) + str(j))
#     print(" ".join(line))


# # Q77. Ticket Price Grid - odd seats 100, even seats 150
# rows, seats = 2, 5
# for i in range(rows):
#     line = []
#     for j in range(1, seats + 1):
#         line.append("100" if j % 2 == 1 else "150")
#     print(" ".join(line))


# # Q78. Classroom Attendance Summary - totals and highest-attendance student
# att = [["P", "A", "P", "P"], ["A", "P", "A", "P"]]
# best, best_i = -1, 0
# for i in range(len(att)):
#     p = 0
#     for d in att[i]:
#         if d == "P":
#             p += 1
#     print(f"Student {i + 1}: Present={p} Absent={len(att[i]) - p}")
#     if p > best:
#         best, best_i = p, i
# print(f"Highest attendance: Student {best_i + 1}")


# # Q79. Duplicate Character Detector - repeated chars (no count()/set())
# s = "BANANA"
# res = []
# for i in range(len(s)):
#     later = False
#     earlier = False
#     for j in range(len(s)):
#         if j > i and s[j] == s[i]:
#             later = True
#         if j < i and s[j] == s[i]:
#             earlier = True
#     if later and not earlier:
#         res.append(s[i])
# print("Repeated characters:", ", ".join(res))


# # Q80. First Repeated Character - first char that appears again
# s = "BANANA"
# found = False
# for i in range(len(s)):
#     for j in range(i + 1, len(s)):
#         if s[i] == s[j]:
#             print(s[i])
#             found = True
#             break
#     if found:
#         break


# # Q81. Remove Duplicate Characters - keep each char once
# s = "BANANA"
# result = ""
# for c in s:
#     exists = False
#     for r in result:
#         if r == c:
#             exists = True
#     if not exists:
#         result += c
# print(result)


# # Q82. Anagram Checker - compare character frequencies (no sorted/set/Counter)
# a, b = "listen", "silent"
# ok = len(a) == len(b)
# if ok:
#     for ch in a:
#         fa = fb = 0
#         for x in a:
#             if x == ch:
#                 fa += 1
#         for y in b:
#             if y == ch:
#                 fb += 1
#         if fa != fb:
#             ok = False
# print("Anagram" if ok else "Not Anagram")


# # Q83. Common Words - words present in both sentences
# s1, s2 = "red blue green".split(), "blue yellow red".split()
# res = []
# for a in s1:
#     for b in s2:
#         if a == b:
#             res.append(a)
# print(", ".join(res))


# # Q84. Duplicate Words - repeated words (no count())
# words = "this is a test this".split()
# res = []
# for i in range(len(words)):
#     later = earlier = False
#     for j in range(len(words)):
#         if j > i and words[j] == words[i]:
#             later = True
#         if j < i and words[j] == words[i]:
#             earlier = True
#     if later and not earlier:
#         res.append(words[i])
# print(", ".join(res))


# # Q85. Unique Words - words occurring exactly once
# words = "this is a test this".split()
# res = []
# for i in range(len(words)):
#     f = 0
#     for j in range(len(words)):
#         if words[i] == words[j]:
#             f += 1
#     if f == 1:
#         res.append(words[i])
# print(", ".join(res))


# # Q86. Palindrome Word Analyzer - check palindromes via char comparisons (no slicing)
# words = "madam level apple".split()
# for w in words:
#     is_pal = True
#     i, j = 0, len(w) - 1
#     while i < j:
#         if w[i] != w[j]:
#             is_pal = False
#         i += 1
#         j -= 1
#     print(w, "is a palindrome" if is_pal else "is not a palindrome")


# # Q87. Longest Palindromic Word - longest palindrome among words
# words = "madam level racecar apple".split()
# best = ""
# for w in words:
#     is_pal = True
#     i, j = 0, len(w) - 1
#     while i < j:
#         if w[i] != w[j]:
#             is_pal = False
#         i += 1
#         j -= 1
#     if is_pal and len(w) > len(best):
#         best = w
# print(best)


# # Q88. Maximum Common Character - highest matching frequency, matching freq = min(freq in a, freq in b)
# # Tie rule: the character that appears first in the first string wins.
# a, b = "ABCA", "BCAD"
# best_c, best_f = "", 0
# for i in range(len(a)):
#     seen = False
#     for k in range(i):
#         if a[k] == a[i]:
#             seen = True
#     if seen:
#         continue
#     fa = fb = 0
#     for x in a:
#         if x == a[i]:
#             fa += 1
#     for y in b:
#         if y == a[i]:
#             fb += 1
#     f = fa if fa < fb else fb
#     if f > best_f:
#         best_c, best_f = a[i], f
# print(f"{best_c} (matching frequency {best_f})")


# # Q89. Most Repeated Character - highest frequency (no count/max/set)
# s = "BANANA"
# best_c, best_f = "", 0
# for ch in s:
#     f = 0
#     for c in s:
#         if c == ch:
#             f += 1
#     if f > best_f:
#         best_c, best_f = ch, f
# print(best_c)


# # Q90. Second Most Repeated Character - second-highest frequency; ties: all printed
# s = "AABBBCC"
# freqs = []
# for i in range(len(s)):
#     f = 0
#     for c in s:
#         if c == s[i]:
#             f += 1
#     freqs.append(f)
# top = 0
# for f in freqs:
#     if f > top:
#         top = f
# second = 0
# for f in freqs:
#     if f < top and f > second:
#         second = f
# res = []
# for i in range(len(s)):
#     if freqs[i] == second:
#         dup = False
#         for k in range(i):
#             if s[k] == s[i]:
#                 dup = True
#         if not dup:
#             res.append(s[i])
# print("Second most repeated:", ", ".join(res), f"(frequency {second})")


# # Q91. Word Pair With Maximum Common Characters
# words = "apple apply orange".split()
# best, pair = -1, None
# for i in range(len(words)):
#     for j in range(i + 1, len(words)):
#         c = 0
#         for ch in words[i]:
#             for x in words[j]:
#                 if ch == x:
#                     c += 1
#                     break
#         if c > best:
#             best, pair = c, (words[i], words[j])
# print(f"{pair[0]} and {pair[1]} (common = {best})")


# # Q92. Number Pair With Common Digits - compare digits of two numbers
# a, b = "12345", "54321"
# c = 0
# for x in a:
#     for y in b:
#         if x == y:
#             c += 1
# print("Common digit count =", c)


# # Q93. Digit Pair Analyzer - classify each ordered digit pair
# s = "58321"
# for a in s:
#     for b in s:
#         if a == b:
#             r = "Equal"
#         elif int(a) > int(b):
#             r = "First greater"
#         else:
#             r = "First smaller"
#         print(a, b, r)


# # Q94. Armstrong Numbers in a Range - 1..N using digit processing
# n = 500
# res = []
# for num in range(1, n + 1):
#     digits = len(str(num))
#     t, s = num, 0
#     while t > 0:
#         d = t % 10
#         p = 1
#         for _ in range(digits):
#             p *= d
#         s += p
#         t //= 10
#     if s == num:
#         res.append(str(num))
# print(", ".join(res))


# # Q95. Prime Pair Generator - prime pairs (a<b<=N) whose sum is also prime
# n = 20
# for a in range(2, n + 1):
#     for b in range(a + 1, n + 1):
#         all_prime = True
#         for x in (a, b, a + b):
#             for d in range(2, x):
#                 if x % d == 0:
#                     all_prime = False
#         if all_prime:
#             print(f"{a}+{b}={a + b}")


# # Q96. Restaurant Table Availability - 1 = available, 0 = occupied
# t = [[1, 0, 1, 1], [0, 0, 1, 0]]
# avail = occ = 0
# for i in range(len(t)):
#     r = 0
#     for j in range(len(t[i])):
#         if t[i][j] == 1:
#             avail += 1
#             r += 1
#         else:
#             occ += 1
#     print(f"Row {i + 1} available = {r}")
# print(f"Available={avail}, Occupied={occ}")


# # Q97. Cinema Seat Booking - O = open, B = booked
# seats = [["O", "B", "O", "O"], ["B", "B", "O", "B"]]
# op = bk = 0
# best, best_i = -1, 0
# for i in range(len(seats)):
#     r = 0
#     for s in seats[i]:
#         if s == "O":
#             op += 1
#             r += 1
#         else:
#             bk += 1
#     if r > best:
#         best, best_i = r, i
# print(f"Open={op}, Booked={bk}")
# print(f"Row {best_i + 1} has most open seats ({best})")


# # Q98. Shopping Cart Price Matrix - customer bills and product quantity totals
# qty = [[2, 1, 3], [1, 4, 2]]
# price = [100, 200, 50]
# prod = [0] * len(price)
# for i in range(len(qty)):
#     bill = 0
#     for j in range(len(price)):
#         bill += qty[i][j] * price[j]
#         prod[j] += qty[i][j]
#     print(f"Customer {i + 1} total = {bill}")
# print("Product quantities:", prod)


# # Q99. Exam Marks Analyzer - totals and highest total student
# m = [[80, 70, 90], [60, 75, 80], [90, 90, 95]]
# best, best_i = -1, 0
# for i in range(len(m)):
#     t = 0
#     for x in m[i]:
#         t += x
#     print(f"Student {i + 1} total = {t}")
#     if t > best:
#         best, best_i = t, i
# print(f"Highest total: Student {best_i + 1} ({best})")


# # Q100. Bus Seat Reservation - 2 seats per row, 1 = booked, 0 = available
# bus = [[1, 0], [0, 0], [1, 1], [0, 1]]
# avail = booked = full = 0
# for row in bus:
#     b = 0
#     for s in row:
#         if s == 1:
#             booked += 1
#             b += 1
#         else:
#             avail += 1
#     if b == len(row):
#         full += 1
# print(f"Available={avail}, Booked={booked}, Fully booked rows={full}")


# # Q101. Pattern + Condition Challenge - A main diagonal, B opposite; center (both) = A
# n = 5
# for i in range(n):
#     line = []
#     for j in range(n):
#         if i == j:
#             line.append("A")
#         elif i + j == n - 1:
#             line.append("B")
#         else:
#             line.append("-")
#     print(" ".join(line))


# # Q102. Character Pyramid - progressively larger centered portions of a string
# s = "ABCDE"
# n = len(s)
# for i in range(1, n + 1, 2):
#     row = ""
#     for j in range(i):
#         row += s[j]
#     print(" " * ((n - i) // 2) + row)


# # Q103. Word Pyramid - progressively larger groups of words
# w = "I love Python code".split()
# for i in range(1, len(w) + 1):
#     line = ""
#     for j in range(i):
#         line += w[j] + " "
#     print(line.strip())


# # Q104. Reverse Word Pyramid - decreasing groups of words
# w = "I love Python code".split()
# for i in range(len(w), 0, -1):
#     line = ""
#     for j in range(i):
#         line += w[j] + " "
#     print(line.strip())


# # Q105. Word Length Pattern - word followed by stars equal to its length
# for w in "I love Python".split():
#     line = ""
#     for ch in w:
#         line += "*"
#     print(w, line)


# # Q106. Character Frequency Pattern - each char with stars per frequency
# s = "BANANA"
# for i in range(len(s)):
#     seen = False
#     for k in range(i):
#         if s[k] == s[i]:
#             seen = True
#     if seen:
#         continue
#     line = ""
#     for c in s:
#         if c == s[i]:
#             line += "*"
#     print(s[i], line)


# # Q107. Number Triangle With Conditions - E/O, X when row == column
# n = 4
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, i + 1):
#         if i == j:
#             line.append("X")
#         elif (i + j) % 2 == 0:
#             line.append("E")
#         else:
#             line.append("O")
#     print(" ".join(line))


# # Q108. Multiplication Pattern Challenge - multiples of 3 -> X, 5 -> Y, both -> Z
# n = 5
# for i in range(1, n + 1):
#     line = []
#     for j in range(1, n + 1):
#         v = i * j
#         if v % 15 == 0:
#             line.append("Z")
#         elif v % 3 == 0:
#             line.append("X")
#         elif v % 5 == 0:
#             line.append("Y")
#         else:
#             line.append(str(v))
#     print(" ".join(line))


# # Q109. Student Performance Matrix - totals, averages, highs, pass/fail, extremes
# m = [[80, 70, 90], [60, 75, 80], [90, 90, 95]]
# pass_mark = 40
# best_i, worst_i = 0, 0
# totals = []
# for i in range(len(m)):
#     t = 0
#     hi = m[i][0]
#     ok = True
#     for x in m[i]:
#         t += x
#         if x > hi:
#             hi = x
#         if x < pass_mark:
#             ok = False
#     totals.append(t)
#     print(f"Student {i + 1}: Total={t} Avg={t / len(m[i]):.2f} Highest={hi} {'Pass' if ok else 'Fail'}")
# for i in range(len(totals)):
#     if totals[i] > totals[best_i]:
#         best_i = i
#     if totals[i] < totals[worst_i]:
#         worst_i = i
# print(f"Topper: Student {best_i + 1} ({totals[best_i]})")
# print(f"Lowest: Student {worst_i + 1} ({totals[worst_i]})")


# # Q110. Matrix Border and Diagonal Analyzer - total, border, diagonals, inner sum
# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# n = len(m)
# total = border = main = opp = inner = 0
# for i in range(n):
#     for j in range(n):
#         v = m[i][j]
#         total += v
#         if i == 0 or j == 0 or i == n - 1 or j == n - 1:
#             border += v
#         else:
#             inner += v
#         if i == j:
#             main += v
#         if i + j == n - 1:
#             opp += v
# print(f"Total={total}, Border={border}, Main diagonal={main}, Opposite diagonal={opp}, Inner={inner}")


# # Q111. Matrix Comparison - equal/different positions of two matrices
# a = [[1, 2], [3, 4]]
# b = [[1, 5], [3, 8]]
# eq = diff = 0
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if a[i][j] == b[i][j]:
#             eq += 1
#         else:
#             diff += 1
# print(f"Equal positions={eq}, Different positions={diff}")


# # Q112. Matrix Addition - element-wise addition
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
# for i in range(len(a)):
#     line = []
#     for j in range(len(a[i])):
#         line.append(str(a[i][j] + b[i][j]))
#     print(" ".join(line))


# # Q113. Matrix Multiplication - three nested loops
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
# r, c, k = len(a), len(b[0]), len(b)
# res = [[0] * c for _ in range(r)]
# for i in range(r):
#     for j in range(c):
#         for x in range(k):
#             res[i][j] += a[i][x] * b[x][j]
# for row in res:
#     print(" ".join(str(v) for v in row))


# # Q114. Tic-Tac-Toe Board Analyzer - winner / incomplete / draw
# b = [["X", "O", "-"], ["O", "X", "-"], ["-", "-", "X"]]
# winner = None
# for p in ["X", "O"]:
#     for i in range(3):
#         rw = cl = True
#         for j in range(3):
#             if b[i][j] != p:
#                 rw = False
#             if b[j][i] != p:
#                 cl = False
#         if rw or cl:
#             winner = p
#     d1 = d2 = True
#     for i in range(3):
#         if b[i][i] != p:
#             d1 = False
#         if b[i][2 - i] != p:
#             d2 = False
#     if d1 or d2:
#         winner = p
# if winner:
#     print(f"{winner} wins")
# else:
#     empty = False
#     for row in b:
#         for c in row:
#             if c == "-":
#                 empty = True
#     print("Game incomplete" if empty else "Draw")


# # Q115. Word Search Grid - print every position of the target character
# grid = [["A", "B", "C", "A"], ["D", "A", "F", "G"], ["A", "H", "I", "J"]]
# target = "A"
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if grid[i][j] == target:
#             print(f"{target} found at row {i}, column {j}")


# # Q116. Password Character Analyzer - uppercase, lowercase, digits, special
# pw = "AbC123!@"
# up = lo = dg = sp = 0
# for ch in pw:
#     if "A" <= ch <= "Z":
#         up += 1
#     elif "a" <= ch <= "z":
#         lo += 1
#     elif "0" <= ch <= "9":
#         dg += 1
#     else:
#         sp += 1
# print(f"Uppercase={up}, Lowercase={lo}, Digits={dg}, Special={sp}")


# # Q117. Mini Inventory System - product totals and store totals
# inv = [[5, 0, 8], [3, 7, 2]]
# stores = [0] * len(inv[0])
# for i in range(len(inv)):
#     t = 0
#     for j in range(len(inv[i])):
#         t += inv[i][j]
#         stores[j] += inv[i][j]
#     print(f"Product {i + 1} total = {t}")
# print("Store totals:", stores)


# # Q118. Cricket Score Matrix - player totals and highest scorer
# s = [[40, 60, 20, 80], [55, 10, 70, 45], [90, 30, 60, 55]]
# best, best_i = -1, 0
# for i in range(len(s)):
#     t = 0
#     for x in s[i]:
#         t += x
#     print(f"Player {i + 1} total = {t}")
#     if t > best:
#         best, best_i = t, i
# print(f"Highest: Player {best_i + 1} ({best})")


# # Q119. Electricity Usage Analyzer - house totals, month totals, highest reading
# u = [[100, 120, 90], [150, 130, 160]]
# months = [0] * len(u[0])
# hi, hi_h, hi_m = -1, 0, 0
# for i in range(len(u)):
#     t = 0
#     for j in range(len(u[i])):
#         t += u[i][j]
#         months[j] += u[i][j]
#         if u[i][j] > hi:
#             hi, hi_h, hi_m = u[i][j], i, j
#     print(f"House {i + 1} total = {t}")
# print("Month totals:", months)
# print(f"Highest single usage: House {hi_h + 1}, Month {hi_m + 1} ({hi})")


# # Q120. Final Multi-Level Data Analyzer - complete college performance report
# m = [[80, 70, 90], [60, 75, 80], [90, 90, 95]]
# ns, nsub = len(m), len(m[0])
# pass_mark = 40
# totals = []
# sub_tot = [0] * nsub
# sub_hi = [0] * nsub
# sub_lo = [100] * nsub
# print("1. Marks matrix:")
# for row in m:
#     print("  ", row)
# print("2-6. Student-wise report:")
# pc = fc = 0
# for i in range(ns):
#     t = 0
#     for j in range(nsub):
#         v = m[i][j]
#         t += v
#         sub_tot[j] += v
#         if v > sub_hi[j]:
#             sub_hi[j] = v
#         if v < sub_lo[j]:
#             sub_lo[j] = v
#     totals.append(t)
#     avg = t / nsub
#     ok = True
#     for v in m[i]:
#         if v < pass_mark:
#             ok = False
#     if ok:
#         pc += 1
#     else:
#         fc += 1
#     grade = "A" if avg >= 80 else "B" if avg >= 60 else "C" if avg >= 40 else "F"
#     print(f"   Student {i + 1}: Total={t} Avg={avg:.2f} Grade={grade} {'Pass' if ok else 'Fail'}")
# print("7-9. Subject-wise (total / average / highest / lowest):")
# for j in range(nsub):
#     print(f"   Subject {j + 1}: {sub_tot[j]} / {sub_tot[j] / ns:.2f} / {sub_hi[j]} / {sub_lo[j]}")
# bi = wi = 0
# for i in range(ns):
#     if totals[i] > totals[bi]:
#         bi = i
#     if totals[i] < totals[wi]:
#         wi = i
# print(f"10. Topper: Student {bi + 1} ({totals[bi]})")
# print(f"11. Lowest scorer: Student {wi + 1} ({totals[wi]})")
# grand = 0
# for t in totals:
#     grand += t
# print(f"12. Class average: {grand / (ns * nsub):.2f}")
# print(f"13. Pass count={pc}, Fail count={fc}")