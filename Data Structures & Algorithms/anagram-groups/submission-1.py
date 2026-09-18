class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordCount = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            wordCount[key].append(word)

        return list(wordCount.values())


        

        