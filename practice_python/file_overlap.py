
""" This reads two files, one containing prime numbers 
under 1000 and the other containing happy numbers under 1000.
After reading two files, it puts all primes and happy numbers 
in seperate lists. It then looks for numbers that are in common
between these two lists."""

def prime_read():
    with open('primes_under_1000.txt', 'r') as open_file:
        all_text = open_file.read()
        all_text = all_text.split('\n')
        #print(all_text)
        return all_text
#prime_read()

def happy_number_read():
    with open('happy_numbers_under_1000.txt', 'r') as open_file:
        all_text = open_file.read()
        all_text = all_text.split('\n')
        #print(all_text)
        return all_text
#happy_number_read()

def happy_prime_overlap():
    primes = prime_read()
    happy = happy_number_read()
    overlap = []
    for prime in primes:
        if prime in happy:
            overlap.append(prime)
    print("Numbers that overlap are: ")
    print(', '.join(overlap))
    print("There are %d numbers under 1000 which are both prime and happy." % (len(overlap)))
    return overlap
happy_prime_overlap()