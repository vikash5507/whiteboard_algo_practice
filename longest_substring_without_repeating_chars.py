"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""

'''
Solution:
    O(N^3) solution - check all possible substring
'''

s = "abcabcbb"

print(len(s) == len(set(s)))

max_substring_len = [1]

size = len(s)
memo_range = {}


def check_all_substring(l: int, r: int) -> None:
    if l < 0 or r >= size or l >= size or r < 0:
        return

    if (l, r) in memo_range:
        return

    check_all_substring(l + 1, r)
    check_all_substring(l, r - 1)

    if len(set(s[l:r+1])) == r - l + 1:
        memo_range[(l, r)] = True
        max_substring_len[0] = max(max_substring_len[0], r - l + 1)
    else:
        memo_range[(l, r)] = False

    return


check_all_substring(0, size-1)

print(max_substring_len[0])

'''
Solution 2:
    O(N) solution using sliding window technique - change start_idx of window when duplicate chars encountered 
'''
s = "abcabcbb"
last_seen_idx = {}
size = len(s)

max_substring_len = 0

start_idx = 0 #starting index of window

for i in range(size):
    if s[i] in last_seen_idx:
        start_idx = max(start_idx, last_seen_idx[s[i]] + 1) #start_idx next to duplicate or already greater start_idx

    max_substring_len = max(max_substring_len, i - start_idx + 1)
    last_seen_idx[s[i]] = i

print(max_substring_len)

