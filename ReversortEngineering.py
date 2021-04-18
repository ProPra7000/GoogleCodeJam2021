T = int(input())

def reverseList(arr, begin, end):
    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1

def iota(arr, N):
    for i in range(N):
        arr.append(i)

for i in range(1, T + 1):
    print('Case #' + str(i) + ': ', end = "")
    data = list(map(int, input().split()))
    N = data[0]
    C = data[1]
    if C < N -1:
        print("IMPOSSIBLE")
        continue
    C -= (N-1)
    arr = []
    iota(arr, 2 * N)
    for j in range(0, N):
        k = min(C, N - j - 1) + j
        reverseList(arr, j, k)
        C -= (k - j)
    if C > 0:
        print("IMPOSSIBLE")
        continue
    ans = [0] * N
    for j in range(N):
        ans[arr[j]] = j

    for j in range(N):
        print(str(ans[j] + 1), end = ' ')
    print()