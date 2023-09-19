def solution(balls, share):
    answer = 1
    numer=1
    baler=1
    for i in range(1,balls+1):
        numer*=i
    for i in range(1, share+1):
        baler*=i
    for i in range(1,balls-share+1):
        answer*=i
    answer = numer//(answer*baler)
    return answer