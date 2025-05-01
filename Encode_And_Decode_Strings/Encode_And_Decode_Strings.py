class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + '#' + s # store len of str
        return encoded_string

    def decode(self, s: str) -> list[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#': # find position of #
                j+=1
            length = int(s[i:j]) # convert len from encoded substring
            i = j + 1 # move past '#'
            j = i + length # Use len to extract the string
            decoded_list.append(s[i:j]) # add the string to the result
            i=j # move to next string
            


        return decoded_list


codec = Solution()
input_strs = ["neet", "code", "love", "you"]
encoded = codec.encode(input_strs)
print(f"Encoded: {encoded}")
decoded = codec.decode(encoded)
print(f"Decoded: {decoded}")