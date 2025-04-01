from typing import List
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Groups anagrams together from the given list of strings.
    
    :param strs: List of input strings
    :return: List of lists, where each sublist contains anagrams
    """
    anagrams = defaultdict(list)
    
    for word in strs:
        sorted_word = tuple(sorted(word))
        anagrams[sorted_word].append(word)
    
    return list(anagrams.values())

test_cases = [
    ["act", "pots", "tops", "cat", "stop", "hat"],
    ["x"],
    [""]
]

for i, test in enumerate(test_cases, 1):
    print(f"Test Case {i}: {group_anagrams(test)}")