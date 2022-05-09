a = 1
b = 34
fibonacci = [a,b]
for i in range(20):
    a, b = b, a+b
    fibonacci.append(b)
print(fibonacci)