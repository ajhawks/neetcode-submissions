class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def compute(op, num1, num2):
            if op == "+":
                return num1 + num2
            if op == "*":
                return num1 * num2
            if op == "-":
                return num1 - num2
            if op == "/":
                return int(num1 / num2)
        operations = ["+", "-", "*", "/"]
        l = []
        for i in tokens:
            if i in operations:
                num2 = l.pop()
                num1 = l.pop()
                output = compute(i, num1, num2)
                l.append(output)
            else:
                l.append(int(i))
        return l[0]
            