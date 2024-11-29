n = int(input("Enter the height of pyramid: "))
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
print(f"Right Half Pyramid of Height {n}")