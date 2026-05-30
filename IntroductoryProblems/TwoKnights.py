import math

def print_num_ways(n: int) -> None:

    for k in range(1,n+1):
        if k == 1:
            print(0)
            continue
        
        area = k ** 2
        sum = math.factorial(area)/(math.factorial(2)*math.factorial(area-2))
        sum -= 4 * (k - 1) * (k - 2)
        print(sum)
        

if __name__ == "__main__":
    n = int(input())

    print_num_ways(n)