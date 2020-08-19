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

def solveAS(exp):
    sub = exp.find('-')
    add = exp.find('+')
    if sub == -1 and add == -1:
        return exp
    a = min(sub, add)
    if add == -1:
        a = sub
    if sub == -1:
        a = add


    sum = True if a == add else False
    left = -1
    right = len(exp)
    for i in range(a-1, -1, -1):
        if exp[i] in operations:
            left= i
            break

    for i in range(a+1, len(exp), 1):
        if exp[i] in operations:
            right = i
            break

    left += 1
    c1 = int(exp[left:a])
    c2 = int(exp[a+1:right])

    diff = 0
    if sum:
        diff = c1 + c2
    else:
        diff = c1 - c2
    newString = exp[:left] + str(diff) + exp[right:]
    return solveAS(newString)

def solveMD(exp):
    mul = exp.find('*')
    div = exp.find('/')
    if mul == -1 and div == -1:
        return exp
    a = min(mul, div)
    if mul == -1:
        a = div
    if div == -1:
        a = mul


    prod = True if a == mul else False

    left = -1
    right = len(exp)
    for i in range(a-1, -1, -1):
        if exp[i] in operations:
            left= i
            break

    for i in range(a+1, len(exp), 1):
        if exp[i] in operations:
            right = i
            break

    left += 1
    c1 = int(exp[left:a])
    c2 = int(exp[a+1:right])

    quot = 0
    if prod:
        quot = c1 * c2
    else:
        quot = int(c1 / c2)
    newString = exp[:left] + str(quot) + exp[right:]
    return solveMD(newString)

def solvePower(exp):
    a = exp.find('^')

    if a == -1:
        return exp

    left = -1
    right = len(exp)
    for i in range(a-1, -1, -1):
        if exp[i] in operations:
            left= i
            break

    for i in range(a+1, len(exp), 1):
        if exp[i] in operations:
            right = i
            break

    left += 1
    c1 = int(exp[left:a])
    c2 = int(exp[a+1:right])

    power = c1 ** c2
    newString = exp[:left] + str(power) + exp[right:]
    return solvePower(newString)

def solveExpression(exp):
    a, b = findParenthesis(exp)
    if a != -1:
        exp = exp[:a-1] + solveExpression(exp[a:b]) + exp[b+1:]
    exp = solvePower(exp)
    exp = solveMD(exp)
    exp = solveAS(exp)
    return exp



exp = getInput()
print(solveExpression(exp))
