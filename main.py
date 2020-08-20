operations = ['-', '+', '/', '*', '^']
debug = False
def getInput():
    ''' Prompts the user for input and returns the input'''

    exp = input("Enter a valid math expression or enter 'exit': ")
    return exp

def findParenthesis(exp):
    ''' Finds the first instance of parentheses in exp and returns the index+1
        of the left parentheses and the index of the right parentheses.
        If no parentheses are present, returns -1,-1
    '''

    # a is the index of the first left parentheses
    a = exp.find('(')
    if a == -1:
        return -1, -1

    # makes sure to find the outermost parentheses
    left = 0
    right = 0
    for i in range(len(exp)):
        if exp[i] == '(':
            left += 1
        if exp[i] == ')':
            right += 1
        if left > 0 and left == right:
            return a+1, i

    # should never reach here. If it does, we are missing parentheses
    raise Exception("Missing Parentheses")

def solveAS(exp):
    if debug: print('AS', exp)
    ''' Simplifies the addition and subtraction in exp from left to right
        Returns the simplified expression
    '''
    sub = exp.find('-')
    add = exp.find('+')


    # allows for leading minus and plus signs
    if sub == 0:
        sub = exp[1:].find('-')
    if add == 0:
        return solveAS(exp[1:])

    if sub == -1 and add == -1:
        return exp

    # allows to simplify in order
    a = min(sub, add)
    if add == -1:
        a = sub
    if sub == -1:
        a = add

    # gets the two terms to the left and right of the operation
    sum = True if a == add else False
    left = -1
    right = len(exp)
    for i in range(a-1, -1, -1):
        if exp[i] in operations:
            left= i
            if exp[i] == '-':
                left -= 1
            break

    for i in range(a+1, len(exp), 1):
        if exp[i] in operations:
            if i == a+1:
                continue
            right = i
            break

    left += 1
    c1 = float(exp[left:a])
    c2 = float(exp[a+1:right])

    # simplifies the sum and difference and returns the modified exp, doing
    # any more sum and differences
    diff = 0
    if sum:
        diff = c1 + c2
    else:
        diff = c1 - c2
    newString = exp[:left] + str(diff) + exp[right:]
    return solveAS(newString)

def solveMD(exp):
    if debug: print('MD', exp)
    ''' Almost identical to the solveAD function, just with multiplication and
        division. Returns the simplified expression
    '''
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
            if exp[i] == '-':
                left -= 1
            break

    for i in range(a+1, len(exp), 1):
        if exp[i] in operations:
            if i == a+1:
                continue
            right = i
            break

    left += 1
    c1 = float(exp[left:a])
    c2 = float(exp[a+1:right])

    quot = 0
    if prod:
        quot = c1 * c2
    else:
        if c2 == 0:
            raise Exception('Divide By Zero')
        quot = float(c1 / c2)
    newString = exp[:left] + str(quot) + exp[right:]
    return solveMD(newString)

def solvePower(exp):
    if debug: print('Power', exp)
    '''
        Simplifies the first exponent in exp, if at all. If no exponent, returns
        exp
    '''
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
            if i == a+1:
                continue
            right = i
            break

    left += 1
    c1 = float(exp[left:a])
    c2 = float(exp[a+1:right])

    power = c1 ** c2
    newString = exp[:left] + str(power) + exp[right:]
    return solvePower(newString)

def solveExpression(exp):
    if debug: print('Expression', exp)
    ''' Returns the simplified and final expression'''
    a, b = findParenthesis(exp)
    if a != -1:
        # allows for multiplication adjacent to parentheses, example: 2(4)
        # becomes 2*4
        beforeParenthesis = a -2
        left = exp[:a-1]
        if beforeParenthesis >= 0 and exp[beforeParenthesis] not in operations:
           left = exp[:a-1] + '*'
        exp = left + solveExpression(exp[a:b]) + exp[b+1:]
        exp = solveExpression(exp)
    exp = solvePower(exp)
    exp = solveMD(exp)
    exp = solveAS(exp)
    return exp


def main():
    while True:
        exp = getInput()
        if exp == 'exit':
            break
        try:
            print("Answer: " + solveExpression(exp))
        except Exception as ex:
            print("Error:", ex)

if __name__ == '__main__':
    main()
