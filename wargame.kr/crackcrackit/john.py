import itertools
chrs = 'abcdefghijklmnopqrstuvwxyz0123456789'
min_length, max_length = 2, 5

for n in range(min_length, max_length+1):
    for xs in itertools.product(chrs, repeat=n):
        print('G4HeulB'+''.join(xs))
