# def butterfly_pattern(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print("*", end="")
#         for j in range(1, 2 * n - 2 * i + 1):
#             print(" ", end="")
#         for j in range(1, i + 1):
#             print("*", end="")
#         print()

#     for i in range(n, 0, -1):
#         for j in range(1, i + 1):
#             print("*", end="")
#         for j in range(1, 2 * n - 2 * i + 1):
#             print(" ", end="")
#         for j in range(1, i + 1):
#             print("*", end="")
#         print()

n = int(input("Enter the number of rows: "))
# butterfly_pattern(n)

for i in range(1,n):
    print("*"*i,end="")
    print(" "*((n-i)*2),end="")
    print("*"*i)
for i in range(n,0,-1):
    print("*"*i,end="")
    print(" "*((n-i)*2),end="")
    print("*"*i)

