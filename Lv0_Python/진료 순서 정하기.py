def solution(emergency):
    answer = []
    rest=sorted(emergency,reverse=True)
    
    for i in emergency:
        answer.append(rest.index(i)+1)
    
    return answer