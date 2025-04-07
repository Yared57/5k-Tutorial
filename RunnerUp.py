if __name__ == '__main__':
    n = int(input())
    listg = []
    listg = list(map(int, input().split()))
    listg.sort()
    g = listg[-1]
    y = 0
    for i in range(n):
        if listg[i] == g:
            y = i
            break
    print(listg[y - 1])
