class Solution:
    def interpret(self, command: str) -> str:
        result = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                result.append("G")
            elif command[i] == '(' and command[i + 1] == ')':
                result.append("o")
                i += 1
            elif command[i] == '(' and command[i + 1] == 'a':
                result.append("al")
                i += 1
            i += 1
        return ''.join(result)