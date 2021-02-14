mixed=[1,2,3,4,5,"word1",'woed2','word3']
print(mixed)
mixed.append(9)
print(mixed)
mixed.insert(8,"word4")
print(mixed)
mixed.extend("word5")
print(mixed)
print(mixed[1])
print(mixed[1:5])
mixed.extend(["word6",'word7'])
print(mixed)
mixed2=['apple','orange','banana']
mixed3=mixed+mixed2
print(mixed3)
mixed.append(mixed2)
print(mixed)
mixed.pop()
print(mixed)
mixed.pop()
print(mixed)
del mixed[5]
print(mixed)
mixed.remove('woed2')
print(mixed)
mixed.insert(5,"word2")
print(mixed)
if 'word2' in mixed:
    print(True)
else:
    print(False)
    

