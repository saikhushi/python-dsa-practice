class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]  # last valid palindrome
        
        longest = ""
        for i in range(len(s)):
            # Odd length palindrome
            odd = expandAroundCenter(i, i)
            # Even length palindrome
            even = expandAroundCenter(i, i+1)
            
            # Pick the longest among current and previous
            longest = max(longest, odd, even, key=len)
        
        return longest
