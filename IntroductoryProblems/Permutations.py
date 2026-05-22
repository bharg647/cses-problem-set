

def print_permutation(n: int) -> None:
    
    if n==1:
        print("1")
        return
    elif n <= 3:
        print("NO SOLUTION")
        return

    arr = []
    for x in range(1,n+1):
        arr.append(x)


    flip = False
    permutation = []

    for i in range((len(arr)+1)//2):
        if arr[i] == arr[len(arr)-i-1]:
            permutation.insert(i, arr[i])
            break
        
        if not flip:
            permutation.insert(0, arr[i])
            permutation.append(arr[len(arr)-i-1])
            flip = True
        else:
            permutation.insert(0, arr[len(arr)-i-1])
            permutation.append(arr[i])
            flip = False
    
    print(" ".join(map(str, permutation)))



        


if __name__ == "__main__":
    n = int(input())

    print_permutation(n)