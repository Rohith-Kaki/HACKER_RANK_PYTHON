if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    array = sorted(set(arr))
    runner_up = array[-2]
    print(runner_up)
