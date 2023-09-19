def solution(numer1, denom1, numer2, denom2):
    answer = []
    denom_n=0
    for i in range(max(denom1, denom2),(denom1*denom2)+1):
        if i % denom1==0 and i%denom2==0:
            denom_n=i
            break
    numer_n = numer1*(denom_n//denom1)+numer2*(denom_n//denom2)
    for i in range(min(numer_n,denom_n),1,-1):
        if denom_n % i==0 and numer_n %i==0:
            numer_n//=i
            denom_n//=i
            break
    answer = [numer_n,denom_n]
    return answer