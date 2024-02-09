"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.

"""

'''
    Solution:
    1. Apply DFS on substring of s in wordDict - pass possible sentence in recursive dfs
    2. append to ans when at end of s
'''

s = "aaaaaaa"
wordDict = ["aaaa","aa","a"]

words_set = set(wordDict)

sentences = []


def dfs_substring(word: str, sentence: str) -> None:
    if not word:
        return

    if word in words_set:
        if not sentence:
            sentences.append(word)
        else:
            sentences.append(sentence + " " + word)
        #return

    for i in range(1, len(word)):
        prefix = word[:i]
        suffix = word[i:]

        # if prefix in words_set and suffix in words_set:
        #     if not sentence:
        #         sentences.append(prefix + " " + suffix)
        #     else:
        #         sentences.append(sentence + " " + prefix + " " + suffix)
        #     #return

        if prefix in words_set:
            if not sentence:
                dfs_substring(suffix, prefix)
            else:
                dfs_substring(suffix, sentence + " " + prefix)

    return


dfs_substring(s, "")
print(sentences)
