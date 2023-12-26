class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            pos = i
            for j in range(i, len(heights)):
                if heights[pos] < heights[j]:
                    pos = j
            heights[pos], heights[i] = heights[i], heights[pos]
            names[pos], names[i] = names[i], names[pos]
        return names
        """
        for i in range(len(heights)):
            for j in range(len(heights) - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
        return names"""
