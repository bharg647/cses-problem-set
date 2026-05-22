
def print_missing_number(n: int, nums: set) -> None:

    for x in range(1,n+1):
        if x not in nums:
            print(x)
            return


if __name__ == "__main__":
    n = int(input())

    nums = set(map(int, input().split(" ")))

    print_missing_number(n, nums)