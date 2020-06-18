import itertools

chars = 'ab1'
n = 8

with open('wordlist.txt', 'w') as documento:
    for xs in itertools.product(chars, repeat=n):
        documento.write(f"{''.join(xs)} \n")

