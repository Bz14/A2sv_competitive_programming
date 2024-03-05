class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", 
            "9" : "wxyz"
        }
        n = len(digits)
        ans = []
        path = []
        def combination(idx):
            if len(path) == n:
                ans.append(''.join(path))
                return

            for char in phone[digits[idx]]:
                path.append(char)
                combination(idx + 1)
                path.pop()
        if n == 0:
            return []
        combination(0)
        return ans
