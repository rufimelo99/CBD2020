n_initials={}

with open('female-names.txt', 'r') as reader:
    for line in reader:
        first_letter = line[0].upper()

        if first_letter not in n_initials.keys():
            n_initials[first_letter]=0
        n_initials[first_letter]+=1

with open('initials4redis.txt', 'w') as writer:
    for key, value in n_initials.items():
        writer.write(f'SET {key} {value}\n')


