file = open('example.txt', 'r')
f = file.read().strip()

val = {'A': 247, 'B': 383, 'C': 156, 'D': 512}
    
stack = []
i = 0

while i < len(f):
    if f[i] in val:
        stack.append(val[f[i]])
        i += 1
    elif f[i] == '(':
        stack.append('(')
        i += 1
    elif f[i] == ')':
        i += 1
        if f[i] == '{':
            j = i + 1
            while f[j] != '}':
                j += 1
            mul = int(f[i+1:j])
            i = j + 1
                
            gs = 0
            while stack and stack[-1] != '(':
                gs += stack.pop()
                
            if stack and stack[-1] == '(':
                stack.pop()
            
            stack.append( gs%1000 * mul) #part01 is gs%1 (wla ne7i MOD)
    else:
        i += 1
    
print(sum(stack))

