def isBiggerThanAny(l: list[int], x: int) -> list[int]:
    l.sort(reverse=True)
    res = []
    for i, val in enumerate(l):
        if val < x:
            return res + [x] + l[i:-1]
        else:
            res.append(val)
    return res


file1 = open('input.txt', 'r')

# Using for loop
print("Using for loop")
max: list[int] = [0, 0, 0]
tmp: int = 0

for line in file1:
    l = line.strip()
    if l == "":
        max = isBiggerThanAny(max, tmp)
        tmp = 0
    else:
        tmp += int(l)
    print(f"Line: {l}, tmp {tmp}, max {max}")

print("FINAL RESULT", max, max[0] + max[1] + max[2])
