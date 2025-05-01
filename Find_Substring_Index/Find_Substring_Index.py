def find_substring_index(foo: str, bar: str) -> int:
    if not bar or not foo:
        raise ValueError("Value passed is empty.")

    
    for i in range(len(foo) - len(bar) + 1): # range is exclusive, so need +1
        if foo[i: i + len(bar)] == bar: # : is start inclusive end exclusive so need + i
            return i


    return -1  


foo = "ilovecode"
bar = "love"
print(find_substring_index(foo, bar))  # Expected output: 1