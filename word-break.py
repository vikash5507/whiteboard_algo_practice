"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique

"""

"""
Solution:
        1. Apply DFS search of substring of s in wordDict
        2. Add memoization to reuse already evaluated string
"""

s = "goalspecial"
wordDict = ["go","goal","goals","special"]

words_set = set(wordDict)

words_concat_mem = {}

def dfs_substring(word: str) -> bool:
    if not word:
        return True

    if word in words_concat_mem:
        return words_concat_mem[word]

    if word in words_set:  # if exact same word present in wordDict
        return True

    words_concat_mem[word] = False
    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]

        if prefix in words_set and suffix in words_set:
            words_concat_mem[word] = True
            return True
        if prefix in words_set and dfs_substring(suffix):
            words_concat_mem[word] = True
            return True

    return words_concat_mem[word]

print(dfs_substring(s))
