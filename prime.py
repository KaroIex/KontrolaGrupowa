class PrimeNumberFinder:
    def __init__(self, n):
        self.n = n


def is_prime(self, num):
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

  def print(self):
      for num in range(2, self.n, self.n + 1):
          is_prime = True
          for i in range(2, num):
              if num % i == 0:
                  is_prime = False
                  break
              if is_prime:
                  print(num)

    