class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        visited_index = set()
        result = []

        for strs_element in strs:
            sorted_str = sorted(strs_element)
            sorted_strs.append(''.join(sorted_str))

        for i in range(len(sorted_strs)):
            if i in visited_index:
                continue
            group = [strs[i]]
            visited_index.add(i)
            for j in range(i+1, len(sorted_strs)):
                if j in visited_index:
                    continue

                if(sorted_strs[i] == sorted_strs[j]):
                    group.append(strs[j])
                    visited_index.add(j)
            result.append(group)

        return result