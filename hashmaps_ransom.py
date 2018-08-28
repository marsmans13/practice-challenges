def checkMagazine(magazine, note):
    d = {}
    for word in magazine:
        if d.get(word):
            d[word] += 1
        else:
            d[word] = 1
    print(d)
    
    for word in note:
        if word not in d or d[word] < 1:
            print("No")
            return None
        else:
            d[word] -= 1
        print(d)
    print("Yes")

print(checkMagazine(['hello', 'my', 'name', 'is', 'sam'], ['hello', 'my', 'name', 'is', 'henry']))

l1 = 'tonight it is the night tonight'.split()
l2 = 'tonight is the night'.split()

print(checkMagazine(l1, l2))