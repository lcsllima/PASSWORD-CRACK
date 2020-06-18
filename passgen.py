import itertools

letras = 'abcde1234'
n = 8

for xs in itertools.product(letras, repeat=n):
    print(''.join(xs))