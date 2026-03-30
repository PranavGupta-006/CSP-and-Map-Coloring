import itertools

letters = ['T','W','O','F','U','R']
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    d = dict(zip(letters, perm))
    
    if d['T'] == 0 or d['F'] == 0:
        continue
    
    two = 100*d['T'] + 10*d['W'] + d['O']
    four = 1000*d['F'] + 100*d['O'] + 10*d['U'] + d['R']
    
    if two + two == four:
        print(d)
        break