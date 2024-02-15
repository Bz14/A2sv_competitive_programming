class Solution:
    def interpret(self, command: str) -> str:
        result = []
        i = 0
        for i, st in enumerate(command):
            if st == 'G':
                result.append("G")
            elif st == '(' and command[i + 1] == ')':
                result.append("o")
            elif st == '(' and command[i + 1] == 'a':
                result.append("al")
        return ''.join(result)