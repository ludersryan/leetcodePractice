class Solution(object):
    def substrOccuranceCount(self, text: str, word: str) -> int:
        if not text or len(word) > len(text):
            raise ValueError("text is None or word > text.")
        
        #if text == word, return 1
        #hard code approach:
        #go char by char and check if char + len(word) - 1 substring = word
        result = 0
        if text == word:
            result = 1
            return result
        
        i = 0
        while i < len(text): # better loop would be while i <= len(text) - len(word)
            if text[i:i +len(word)] == word:
                result += 1
            print(text[i:i +len(word)], i)
            
            i += 1

            

        return result
    
test = Solution()
text = ""
word = ""
print(test.substrOccuranceCount(text, word))