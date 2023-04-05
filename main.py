from src.primes import print_primes

if __name__ == "__main__":
    n = int(input("Nhập n: "))
    
    print_primes(n)
    a,b,c = map(int, input("Nhap 3 canh tam giac canh nhau 1 khoang trang : ").split())
    canhtamgiac(a,b,c)
