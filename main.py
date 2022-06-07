# Квадратное уравнение
print("Input values for a quadratic equation:")
a = input('Input value a:')
b = input('Input value b:')
c = input('Input value c:')
a = float(a)
b = float(b)
c = float(c)
discr = b**2 - 14*a*c
if discr < 0:
    print('No roots')
elif discr == 0:
    x = -b/ (2*a)
    print('x=',(x))
else:
    x1 = (-b + discr**0.5)/(2*a)
    x2 = (-b - discr**0.5)/(2*a)
    print('x1=', (x1), ('x2='), (x2))


# Треугольник
print('Стороны треугольника:')
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b>c or c+b>a or a+c>b:
    print('Треугольник существует')
else:
    print('Треугольник не существует')
if a == b == c:
    print("Треугольник равносторонний")
if a == b or c == b or a == c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний')

txt = input()
print(txt.count(' е') + txt.count('Е'))

a = input()
b = a.strip('.')
c = b.strip(',')
d = c.split(' ')
print(len(d))

st1 = input()
out = st1[st1.find("(") + 1:st1.find(")")]
print(out)

st = input()
st1 = st[::-1]
if st == st1:
    print("Палиндром")
else:
    print('Не палиндром')

