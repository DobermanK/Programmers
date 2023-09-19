def solution(array):
    answer = 0
    count_arr = [0]*(max(array)+1)
    
    for i in array:
        count_arr[i]+=1
    
    max_cnt = max(count_arr)
    for i in range(len(count_arr)):
        if count_arr[i] == max_cnt:
            if answer == 0:
                answer = i
            else: answer=-1
    return answer