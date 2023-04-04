import pytest
from src.primes import is_prime, print_primes
from unittest.mock import patch
import os

@pytest.fixture
def mockis_prime(mocker, is_prime):
    mocker.patch("src.primes.is_prime", return_value=is_prime)
    
@pytest.mark.parametrize(
    "a, is_prime, prime",
    [
        (2, True, True),
        (3, True, True),
        (21, False, False),
        (55, False, False),
        (97, True, True),
    ],
)
@pytest.mark.usefixtures("mockis_prime")
def test_primes(a, prime):
    assert is_prime(a) == prime
 
@pytest.mark.parametrize(
    "n, output",
    [
        (2, [2]),  # Test case 2: Chỉ có số nguyên tố 2 trong phạm vi từ 2 đến 2
        (10, [2, 3, 5, 7]),  # Test case 3: Các số nguyên tố trong phạm vi từ 2 đến 10
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]), # Test case 3: Các số nguyên tố trong phạm vi từ 2 đến 50
        (500, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499]) # Test case 3: Các số nguyên tố trong phạm vi từ 2 đến 500
    ],
)
def test_prime_numbers(n, output):
    assert print_primes(n) == output


