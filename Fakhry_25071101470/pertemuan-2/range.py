x = range(10)

x = range(3, 10)

x = range(3, 10, 2)

r = range(0, 10, 2)
print(len(r))

r = range(0, 10, 2)
print(6 in r)
print(7 in r)

r = range(10)
print(r[2])
print(r[:3])

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

for i in range(10):
  print(i)