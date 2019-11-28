functions = []
for i in range(10):
    functions.append(lambda i:i)

for i,k in enumerate(functions):
    print (k(i))



test_val  = lambda: 123

print(test_val())
