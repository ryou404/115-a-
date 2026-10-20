n = int(input())
scores = list(map(int, input().split()))
total = 0
passed = 0
for s in scores:
    total += s
    if s >= 60:
        passed += 1
avg = total / n
print(f"{avg:.2f}")
print(passed)