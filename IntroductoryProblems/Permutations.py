from collections import deque

def print_permutation(n: int) -> None:
    
    if n==1:
        print("1")
        return
    elif n <= 3:
        print("NO SOLUTION")
        return

    flip = False
    permutation = deque([])

    for i in range(1,((n+1)//2)+1):
        if i == n-i+1:
            permutation.insert(i-1, i)
            break
        
        if not flip:
            permutation.appendleft(i)
            permutation.append(n-i+1)
            flip = True
        else:
            permutation.appendleft(n-i+1)
            permutation.append(i)
            flip = False
    
    print(" ".join(map(str, permutation)))



        


if __name__ == "__main__":
    n = int(input())

    print_permutation(n)