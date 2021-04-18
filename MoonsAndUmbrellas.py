def payFor(a, b, x, y):
    if (a == 'C' and b == 'J'):
        return x
    if (a == 'J' and b == 'C'):
        return y
    return 0

k = int(input())

for i in range(1, k + 1):
    print("Case #" + str(i) + ': ', end = '')
    ans = 0
    l = 0
    r = 0
    arr = []
    data = list(map(str, input().split()))
    cj = int(data[0])
    jc = int(data[1])
    s = data[2]
    s = '#' + s + "#"
    for j in range(1, len(s)):
        currChar = s[j]
        prevChar = s[j - 1]
        ans += payFor(prevChar, currChar, cj, jc)
        if (prevChar != '?' and currChar == '?'):
            l = j
        elif (prevChar =='?' and currChar != '?'):
            arr.append([l, j - 1])
    for j in range(0, len(arr)):
        l = arr[j][0]
        r = arr[j][1]
        if (l == 1 or r == len(s) - 2):
            continue
        ans += payFor(s[l - 1], s[r + 1], cj, jc)
    print(str(ans), end = '')
    print()