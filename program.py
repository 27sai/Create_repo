n=int(input())
c=0
for i in range(1,n):
    if n%i==0:
        c+=1
if c==1:
    print("Mission Passed")
else:
    print("Mission Failed")   