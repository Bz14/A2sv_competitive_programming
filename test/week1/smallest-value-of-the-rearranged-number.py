class Solution:
    def smallestNumber(self, num: int) -> int:
        numbers = []
        res = 0
        original_num = num
        num = abs(num)
        while num > 0:
            numbers.append(num % 10)
            num //= 10
        if original_num > 0:
            numbers.sort()
            if numbers[0] == 0:
                for i in range(1, len(numbers)):
                    if numbers[i] > numbers[0]:
                        numbers[0], numbers[i] = numbers[i], numbers[0]
                        break
            res = int(''.join([str(num) for num in numbers]))
        elif original_num < 0:
            numbers.sort(reverse = True)
            res = -(int(''.join([str(num) for num in numbers])))
        return res


