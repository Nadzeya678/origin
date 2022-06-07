# This is a sample Python script.

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
