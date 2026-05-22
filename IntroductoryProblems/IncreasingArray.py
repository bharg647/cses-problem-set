
def print_min_moves(arr: list) -> None:
    min_moves = 0

    for i,x in enumerate(arr):
        if i == 0:
            continue
        
        if arr[i-1]>x:
            diff = arr[i-1]-x
            x += diff
            arr[i] = x
            min_moves += diff
        
    print(min_moves)



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(" ")))

    print_min_moves(arr)