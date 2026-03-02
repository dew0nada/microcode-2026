file =open('data/in_01.txt', 'r')
lines = file.read().strip().split('\n')
    
t = int(lines[0])
f = [int(x) for x in lines[1:]]
fset = set(f)

for num in f:
    m = t - num
    if m in fset:
        print(f"sol: {num * m}")
        break