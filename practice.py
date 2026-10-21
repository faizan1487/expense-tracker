class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}

        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i in anagrams:
                anagrams[sorted_i].append(i)
            else:
                anagrams[sorted_i] = [i]


        anagrams_list = []

        for value in anagrams.values():
            anagrams_list.append(value)


        return anagrams_list


        


sol = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(sol.groupAnagrams(strs))
