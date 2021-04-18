def ask(a, b, c):
    print(str(a) + ' ' + str(b) + ' ' + str(c))
    d = int(input())
    return d

def calcMinMax():
    for i in range(0, n):
        ans[i] = i + 1
    r = n - 1
    for i in range(2, n):
        med = ask(ans[0], ans[1], ans[2])
        for j in range(0, 3):
            if med == ans[j]:
                temp = ans[j]
                ans[j] = ans[r]
                ans[r] = temp
                r -= 1
                break
    temp = ans[1]
    ans[1] = ans[n - 1]
    ans[n - 1] = temp

def partition(lo, hi):
    pivot = ans[hi]
    i = lo
    for j in range(lo, hi):
        if ask(ans[0], ans[j], pivot) == ans[j]:
            temp = ans[i]
            ans[i] = ans[j]
            ans[j] = temp
            i += 1
    temp = ans[i]
    ans[i] = ans[hi]
    ans[hi] = temp
    return i

def quickSort(lo, hi):
    if lo < hi:
        p = partition(lo, hi)
        quickSort(lo, p - 1)
        quickSort(p + 1, hi)

data = list(map(int, input().split()))
t = data[0]
n = data[1]
q = data[2]
ans = [0] * 100
for h in range(1, t + 1):
    calcMinMax()
    quickSort(1, n - 2)
    for i in range(0, n):
        print(str(ans[i]) + " ", end = "")
    print()
    verdict = int(input())
    if verdict == 1:
        continue