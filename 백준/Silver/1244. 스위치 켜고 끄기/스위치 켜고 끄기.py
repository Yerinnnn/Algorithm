def switch(num):
    if status[num] == 0:
        status[num] = 1
    else:
        status[num] = 0
    return


N = int(input())
status = [-1] + list(map(int, input().split()))
student = int(input())

for _ in range(student):
    sex, number = map(int, input().split())
    if sex == 1:
        for i in range(number, N+1, number):
            switch(i)
    elif sex == 2:
        switch(number)
        for k in range(N//2):
            if number + k > N or number - k < 1 : break
            if status[number + k] == status[number - k]:
                switch(number + k)
                switch(number - k)
            else:
                break

for i in range(1, N+1):
    print(status[i], end=" ")
    if i % 20 == 0:  # 20개씩 끊어서 출력
        print()