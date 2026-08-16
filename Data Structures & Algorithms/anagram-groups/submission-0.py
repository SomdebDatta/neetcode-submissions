class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)

        for word in strs:
            sorted_words[''.join(sorted(word))].append(word)
        
        return list(sorted_words.values())