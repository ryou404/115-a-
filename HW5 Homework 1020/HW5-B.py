a, b, k = map(int, input().split())
count = 0
total = 0
for num in range(a, b + 1):
    if num % k == 0:
        count += 1
        total += num
print(f"{count} {total}")