
def weird_alg(n: int) -> None:
    if n == 1:
        return
    
    if n % 2 == 0:
        n /= 2
    else:
        n *= 3
        n += 1
    
    print(int(n), end=" ")
    weird_alg(int(n))


if __name__ == "__main__":
    n = int(input())
    print(n, end=" ")

    weird_alg(n)