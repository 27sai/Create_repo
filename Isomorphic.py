def isomorphic(str1,str2):
    dict1,dict2={},{}
    for x,y in zip(str1,str2):
        if (x in dict1 and dict1[x]!=y) or (y in dict2 and dict2[y]!=x):
            return False
        dict1[x]=y
        dict2[y]=x
    return True
str1='foo'
str2='zok'
print(isomorphic(str1,str2))