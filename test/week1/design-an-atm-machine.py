class ATM:

    def __init__(self):
        self.moneyInAtm = [0] * 5
        self.money = [500, 200, 100, 50, 20]

    def deposit(self, banknotesCount: List[int]) -> None:
        j = 0
        for i in range(len(banknotesCount) - 1, -1, -1):
            self.moneyInAtm[j] += banknotesCount[i]
            j += 1

    def withdraw(self, amount: int) -> List[int]:
        ans = []
        for value, money in zip(self.money, self.moneyInAtm):
            currentMoney =  min(money, amount // value)
            ans.append(currentMoney)
            amount -= (currentMoney * value)
        ans = ans[::-1]
        minusVal = [-val for val in ans]
        if amount == 0:
            self.deposit(minusVal)
            return ans
        else:
            return [-1]



# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)