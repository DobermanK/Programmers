def solution(age):
    answer = ''
    if age//1000: answer+=chr(age//1000+ord("a"))
    if age//100 or answer != '': answer+=chr(age%1000//100+ord("a"))
    if age//10 or answer != '': answer+=chr(age%100//10+ord("a"))
    answer+=chr(age%10+ord("a"))

    return answer