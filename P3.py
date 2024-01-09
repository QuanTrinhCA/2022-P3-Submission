pbuffer = input().split()
customernum = pbuffer.pop(2)
males = pbuffer
females = input().split()
sizeswanted = input().split()
sellable = int()
childs = list()

for male in males:
    malesize = int(male)
    for female in females:
        childs.append((malesize + int(female)) / 2)
        
for requestedsize in sizeswanted:
    for child in childs:
        if child == int(requestedsize):
            childs.remove(child)
            sellable += 1
            break

print(str(sellable))