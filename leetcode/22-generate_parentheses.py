def generateParenthesis(n):

    lst = []

    def calc(string):
        if n*2 == len(string):
            if string not in lst:
                lst.append(string)
            print(lst)
            return

        starts = []
        for i, s in enumerate(string):
            if s == '(':
                starts.append(i)
            if s == ')':
                starts.pop(0)

        for idx in starts:
            calc(string[:idx+1] + ')' + string[idx+1:])

        return
    
    calc('('*n)

    return lst

print(generateParenthesis(3))
print(generateParenthesis(1))