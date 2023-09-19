def solution(lines):
    answer = 0
    line_dis=[0]*201
    for line in lines:
        for i in range(line[0]+100,line[1]+100):
            line_dis[i]+=1
    flag=False
    for i in line_dis:
        if flag:answer+=1
        if i>1:flag=True
        else: flag=False
    return answer