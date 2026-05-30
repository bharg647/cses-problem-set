import math

def print_num_ways(n: int) -> None:

    for k in range(1,n+1):
        if k == 1:
            print(0)
            continue
        elif k == 2:
            print(6)
            continue
        
        area = k ** 2
        sum = (area*(area-1))/2
        sum -= 4 * (k - 1) * (k - 2)
        print(int(sum))
        

if __name__ == "__main__":
    n = int(input())

    print_num_ways(n)
