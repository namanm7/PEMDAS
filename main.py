operations = ['-', '+', '/', '*', '^']

def getInput():
    exp = input("Enter a valid math expression\n")
    return exp

def findParenthesis(exp):
    a = exp.find('(')
    if a == -1:
        return -1, -1
    left = 0
    right = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            left += 1
        if exp[i] == ')':
            right += 1
        if left > 0 and left == right:
            return a+1, i
    return -1, -1

def solveMinus(exp):
    a = exp.find('-')
    if a == -1:
        return exp
    left = 0
    right = len(exp)
    for i in range(a-1, -1, -1):
        if exp[i] in operations:
            left= i
            break

    for i in range(a+1, len(exp), 1):
        if exp[i] in operations:
            right = i
            break
    c1 = int(exp[left:a])
    c2 = int(exp[a+1:right])
    diff = c1 - c2
    return exp[:left] + str(diff) + exp[right:]


def solveExpression(exp):
    a, b = findParenthesis(exp)
    if a != -1:
        exp = exp[:a-1] + solveExpression(exp[a:b]) + exp[b+1:]
    exp = solveMinus(exp)
    return exp



exp = getInput()
print(solveExpression(exp))
