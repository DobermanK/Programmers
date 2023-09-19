def solution(numbers, direction):
    answer = []
    if direction == "right":
        for i in range(-1,len(numbers)-1):
            answer.append(numbers[i])
    else:
        for i in range(0,-1*len(numbers),-1):
            answer.insert(0,numbers[i])
    return answer