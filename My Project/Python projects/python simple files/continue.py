numbersTake = [2, 5, 12, 33, 17]

print("This is the numbers that are still available")
for a in range(1, 20):
    if a in numbersTake:
        continue
    print(a)
