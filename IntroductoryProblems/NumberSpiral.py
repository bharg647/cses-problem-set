def print_number(y: int, x: int) -> None:

    x_bigger = None
    square_index = None
    if y>x:
        square_index = y
        x_bigger = False
    else:
        square_index = x
        x_bigger = True
    
    sum = square_index*(square_index-1)+1
    
    if square_index % 2 == 0:
        # Increasing down/left
        if x_bigger:
            #Change y/row
            sum -= abs(square_index - y)
        else:
            #Change x/column
            sum += abs(square_index - x)

    else:
        #Increasing up/right
        if x_bigger:
            #Change y/row
            sum += abs(square_index - y)
        else:
            #Change x/column
            sum -= abs(square_index - x)

    print(sum)
        


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        y,x = map(int, input().split(" "))

        print_number(y,x)