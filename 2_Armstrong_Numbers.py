#Program 2 - ARMSTRONG NUMBER

print("\tPrinting 3 digit, 4 digit & 5 digit Armstrong Numbers")
print("\t*****************************************************\n")
for num in range(100,100001):
    armst=0
    s=str(num)
    for loop in s:
        digit=int(loop)
        power=len(s)
        armst=armst+digit**power
        
    if num==100:
        print("3 digit Armstrong Numbers:\n")
    elif num==1000:
        print("\n4 digit Armstrong Numbers:\n")
    elif num==10000:
        print("\n5 digit Armstrong Numbers:\n")
        
    if armst==num:
        print(num)