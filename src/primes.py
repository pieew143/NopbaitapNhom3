def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    sqrt = int(n**0.5) + 1
    for i in range(3, sqrt,2 ):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    """In ra danh sách các số nguyên tố trong phạm vi từ 2 đến n."""
    primes = []
    primes.append(2)
    for i in range(3, n + 1, 2):
        if is_prime(i):
            primes.append(i)
    print(primes)
    return primes