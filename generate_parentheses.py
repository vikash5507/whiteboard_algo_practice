"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8

"""

'''
Solution: Recursive solution to generate all permutations
    1. generate all open bracket '(' till its count is less than n
    2. generate all closed bracket ')' till its count is less than current open bracket count
    3. if count of open and closed bracket reaches n then generated permutation string is the one of valid bracket string
'''
n = 8
balanced_brackets = []


def generate_valid_brackets_permutations(n: int, open_count: int, closed_count: int, s: str):
    if open_count == n and closed_count == n:
        balanced_brackets.append(s)

    if open_count < n:
        generate_valid_brackets_permutations(n, open_count + 1, closed_count, s + '(')

    if closed_count < open_count:
        generate_valid_brackets_permutations(n, open_count, closed_count + 1, s + ')')


generate_valid_brackets_permutations(n, 0, 0, '')

print(balanced_brackets)
