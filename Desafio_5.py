a = input('Digite uma palavra: ')
b = ' '.join(k[::-1]
for k in a.split())
print(b)
