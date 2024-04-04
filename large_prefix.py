def longestCommonPrefix(lis):
    n=len(lis)
    prefix=lis[0]
    len_prefix=len(prefix)
    for i in lis[1:]:
        s=i
        while prefix!=s[0:len_prefix]:
            if len_prefix==0:
                return -1
            else:
                len_prefix-=1
                prefix=prefix[0:len_prefix]
    if len(prefix)>0:
        return prefix 
    else:
        return -1
lis=["flower","flow","flight"]
print(longestCommonPrefix(lis))