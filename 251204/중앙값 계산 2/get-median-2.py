N = int(input())
arr = list(map(int, input().split()))

#홀수 번째 수를 지날 때마다 정렬 진행 후 중앙값 출력
for i in range(N):
    if i % 2 == 0:
        #오름차순 정렬
        sorted_arr = sorted(arr[:i + 1])
        #중앙값 출력
        print(sorted_arr[i // 2], end = " ")