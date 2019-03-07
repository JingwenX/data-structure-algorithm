#LINT NO 627 Longest Palindrome

#5 min
#time used: 25min

# abAbAbabazzz


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        """
        Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
        Sol:
        this can be finished in O(n). We just loop over and check if any letter comes in double, and then 
        make a list of all singles, pop it out when meets a double.
        O(52n)
        Worst case: abcdefg....ABCDEFG...abcdefg...ABCDEFG
        Cannot be determined until you meet the very last letter
        """
        if not s:
            return 0
        #init i and list
        i = 0
        singles = []
        while i < len(s):
            count_in_singles = singles.count(s[i])
            if count_in_singles > 0:
                singles.pop(singles.index(s[i]))
            else:
                singles.append(s[i])
            i += 1
        len_longest_palindrome = len(s) - len(singles) + 1
        return len_longest_palindrome

# accepted on second submission
# problem with first submission: used list.index(), which returns value error when encounter no value in list.