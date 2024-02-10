"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).


Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.

"""
from collections import defaultdict

"""
    O(N)
"""
def solve(s):
    freq_count_map = defaultdict(int)
    for c in s:
        freq_count_map[c] += 1

    deletions = 0
    freq_count_set = set()

    # make freq count unique
    for c, count in freq_count_map.items(): # make run for 24 times - O(1)
        _count = count
        while _count > 0 and _count in freq_count_set:  # make run for O(N)
            _count -= 1
            deletions += 1

        freq_count_set.add(_count)

    return deletions


if __name__ == "__main__":
    print(solve("aab"))
    print(solve("aaabbbcc"))
    print(solve("ceabaacb"))
