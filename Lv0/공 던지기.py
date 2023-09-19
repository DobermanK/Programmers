def solution(numbers, k):
    answer = -1
    for _ in range(k):    
        answer+=2
        if answer>len(numbers):
            answer-=len(numbers)
    
    return answer