class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            word_length = len(word)
            encoded_word = str(word_length) + '#' + word
            encoded_string = encoded_string + encoded_word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            j = i+1
            while s[j] != '#':
                j+=1
            word_length = int(s[i:j])
            decoded_word = s[j+1: j+1+word_length]
            decoded_strings.append(decoded_word)
            i = word_length + 1 + j
        return decoded_strings
