if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) #splits the array
    array = sorted(set(arr))    #sorts the array
    runner_up = array[-2]
    print(runner_up)
