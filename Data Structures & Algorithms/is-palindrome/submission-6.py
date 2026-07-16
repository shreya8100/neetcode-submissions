class Solution:
    def isPalindrome(self, s: str) -> bool:

        lower_s = s.lower()
        alpha_numeric_s = "".join(char for char in lower_s if char.isalnum())

        if(len(alpha_numeric_s.strip()) < 1):
            return True

        s_length = len(alpha_numeric_s)
        result = False
        print(alpha_numeric_s)
        for i in range(s_length):
            start = i
            end = s_length - i - 1
            if(alpha_numeric_s[start] == alpha_numeric_s[end]):
                result = True
            else:
                result = False
                break
        
        return result
            