def solution(a, b):
    answer = 2
    while True:
        for i in range(a+1,0,-1):
            if a%i==0 and b%i==0:
                a=a//i
                b=b//i
                continue
        break
    while True:
        if b%5==0:
            b=b//5
        elif b%2==0:
            b=b//2
        else:
            if b==1:answer=1
            break
    return answer