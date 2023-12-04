class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_dict = {}
        for i in range(10):
            num_dict[str(i)]=i
        num_1 = 0
        num_2 = 0
        for num in num1:
            num_1 = num_1 * 10 + num_dict[num]
        for num in num2:
            num_2 = num_2 * 10 + num_dict[num]
        res = num_1 * num_2
        return str(num_1 * num_2)
        