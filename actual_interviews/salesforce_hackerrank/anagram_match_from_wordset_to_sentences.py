"""
wordset = ["the", "bats", "tabs", "in", "cat", "act"]

sentences = ["cat the bats", "in the act", "act tabs in"]

ans = [4,2,4]

"cat the bats" -> cat (2 possible - cat, act) * the (1) * bats (2 possible - bats, tabs)
"in the act" -> in (1) * the (1) * act (2)
"act tabs in" -> act (2) * tabs (2) * in (1)
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countSentences' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY wordSet
#  2. STRING_ARRAY sentences
#

def createCharacterMap(word):
    c_map = {}
    for c in word:
        if c not in c_map:
            c_map[c] = 1
        else:
            c_map[c] += 1
    return c_map


def matchTwoCMap(c_map1, c_map2):
    # print(c_map1.keys(), len(c_map1.keys()), c_map2.keys(), len(c_map2.keys()))
    if len(c_map1.keys()) != len(c_map2.keys()):
        return False
    else:
        for key, value in c_map1.items():
            # print(key, value)
            if key not in c_map2:
                return False
            elif value != c_map2[key]:
                return False
        return True


def countSentences(wordSet, sentences):
    # Write your code here
    # for each word in senetence -> determine from how many words can it be made and multiply them
    wordSetAnagram = []
    for word in wordSet:
        c_map = createCharacterMap(word)

        wordSetAnagram.append(c_map)

    res = []
    # print(wordSetAnagram)
    for sentence_str in sentences:
        match_count = []
        sentence = sentence_str.split(" ")
        # print(sentence)
        for word_sent in sentence:
            # print(word_sent)
            sent_word_c_map = createCharacterMap(word_sent)
            counter = 0
            # print(sent_word_c_map)
            for word_set_c_map in wordSetAnagram:
                if (matchTwoCMap(word_set_c_map, sent_word_c_map)):
                    counter += 1
            match_count.append(counter)

        sent_res = 1
        for v in match_count:
            sent_res = sent_res * v
        res.append(int(sent_res))

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    wordSet_count = int(input().strip())

    wordSet = []

    for _ in range(wordSet_count):
        wordSet_item = input()
        wordSet.append(wordSet_item)

    sentences_count = int(input().strip())

    sentences = []

    for _ in range(sentences_count):
        sentences_item = input()
        sentences.append(sentences_item)

    result = countSentences(wordSet, sentences)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
