import re

print('Digite a função: para exponencial usar ** exemplo: para x² usar x**2')
function = input()

print('Digite um intervalo: [x, y]')
interval = input()

while not re.match('\[{0,1}\d,\d\]{0,1}', interval):
    print('Digite um intervalo válido: [x, y]')
    interval = input()

print('Digite o espaçamento:')
space = int(input())

coords = interval.split(',')
x1 = int(re.sub('\D', '', coords[0]))
x2 = int(re.sub('\D', '', coords[1]))

center = (x2 - x1) / space

ci = []
left = 0
right = center
for item in range(space):
    ci.append((left + right) / 2)
    left = right
    right += center

area = 0
for c in ci:
    calc = function.replace('x', str(c))
    area += eval(calc)

area *= center
print('A área total é: ' + str(round(area, 2)) + ' u.a')