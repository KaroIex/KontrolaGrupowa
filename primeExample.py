import prime

finder = PrimeNumberFinder(100)
finder.print_prime_numbers()

result = finder.is_prime(7)
if result:
    print('7 is a prime number')
else:
    print('7 is not a prime number')