"""
https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75
1657. Determine if Two Strings Are Close
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

"""

from collections import defaultdict

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1) != len(word2):
            return False

        dict1 = defaultdict(int)
        dict2 = defaultdict(int)

        for ch in word1:
            dict1[ch] += 1
        
        for ch in word2:
            dict2[ch] += 1

        for key in dict1:
            if not dict2[key]:
                return False

        if len(dict1) != len(dict2):
            return False
        
        arr1 = dict1.values()
        arr2 = dict2.values()

        arr1.sort()
        arr2.sort()

        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        
        return True

