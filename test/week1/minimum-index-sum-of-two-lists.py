class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = {}
        result = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    common[list1[i]] = i + j
        minIndex = min(common.values())
        for key, value in common.items():
            if value == minIndex:
                result.append(key)
        return result

