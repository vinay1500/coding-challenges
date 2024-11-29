n = int(input("Enter the height of pyramid: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()
print(f"Left Half Pyramid of Height {n}")