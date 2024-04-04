def removeOuterParentheses(s):
    t=0
    res=""
    for i in range(len(s)):
        if s[i]=='(' and t==0:
            t+=1
        elif s[i]=='(' and t>0:
            res+='('
            t+=1
        elif s[i]==')' and t>1:
            res+=')'
            t-=1
        else:
            t=0
    return res
s = "(()())(())(()(()))"
print(removeOuterParentheses(s))