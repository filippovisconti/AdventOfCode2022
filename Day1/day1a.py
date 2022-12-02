file1 = open('input.txt', 'r')

# Using for loop
print("Using for loop")
max: int = 0
tmp: int = 0

for line in file1:
    l = line.strip()
    if l == "":
        if tmp > max:
            max = tmp
        tmp = 0
    else:
        tmp += int(l)
    print(f"Line: {l}, tmp {tmp}, max {max}")

print("FINAL RESULT", max)