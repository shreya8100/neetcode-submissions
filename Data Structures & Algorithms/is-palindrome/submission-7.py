class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaNumS = ''
        isStringPalindrom = False

        for i in range(len(s)):
            if s[i].isalnum():
                alphaNumS = alphaNumS + s[i].lower()
        
        if(len(alphaNumS.strip()) <= 1):
            return True
        
        if(alphaNumS == alphaNumS[::-1]):
            isStringPalindrome = True
        else:
            isStringPalindrome = False
        
        return isStringPalindrome