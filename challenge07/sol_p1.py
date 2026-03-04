def strength(seq):
    return seq.count('1')

file = open("input.txt", "r")
line = [line.strip() for line in file.readlines()]

p = int(line[0])
index = 1
sol = 0

for word in range(p):
    pop = line[index:index+4]
    index += 4

    minisum = 0

    for g in range(1,1001):
        #mini tab strength/index
        st = [(strength(pop[i]),i) for i in range(4)]
        st.sort(key=lambda x: (x[0], x[1]), reverse= True) #max to min

        id1 = st[0][1]
        val1 = pop[id1]
        id2 = st[1][1]
        val2 = pop[id2]

        split = (strength(val1) + strength(val2) ) % 7 + 1
        Offspring1 = val1[0 : split] + val2[split : 8]
        Offspring2 = val2[0 : split] + val1[split : 8]

        strike = (g * 3 + strength(val1)) % 8
        def switch(word, strike):
            if word[strike] == '0':
                s = '1'
            else:
                s = '0'
            new = word[0:strike] + s + word[strike+1 :]
            return new
        Offspring1 = switch(Offspring1, strike)
        Offspring2 = switch(Offspring2, strike)
        
        arraylist= [val1, val2, Offspring1, Offspring2]
        swip = g % 4
        for i in range(4):
            pop[(i+swip)%4] = arraylist[i]
        gensum = sum(int(seq, 2) for seq in pop)

        minisum += gensum

    sol += minisum

print(sol)


