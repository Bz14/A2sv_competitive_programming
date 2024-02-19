class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customer_list = []
        count = defaultdict(int)
        for customer in customers:
            if customer == "Y":
                customer_list.append(1)
            else:
                customer_list.append(0)
        total = sum(customer_list)
        count[0] = total
        for i in range(len(customer_list)):
            if customer_list[i] == 1:
                total -= 1
            else:
                total += 1
            count[i + 1] = total
        minVal = min(count.values())
        for val in count:
            if count[val] == minVal:
                return val
        return 0