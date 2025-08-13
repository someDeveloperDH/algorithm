#수학, 기하학, 피타고라스 정리
#출처 : Waterloo's local Programming Contests

#방법 1 raw - 27분

'''
3,4,5 는 직각삼각형
주어진 3변의 길이로 직각인지 확인

<입력>
한번 입력 여러개의 테스트 케이스
한줄에 3개의 변의 길이
마지막 0 0 0이 테스트 케이스 종료

<출력>
right
wrong

'''
'''
<분석>

사전 지식 필요 -> 직각 삼각형의 조건.
(사전 지식) 빗변의 제곱은 다른 두변 각각의 제곱의 합과 같음
빗변을 어떻게 판단? 가장 긴변

정리 : 세개의 변 중 가장 긴 변의 제곱은 나머지 두변의 각각의 제곱과 같다.
가정 무족건 삼각형이다
'''

import sys

triangles = sys.stdin.read().splitlines() 

for i in range(len(triangles)) :
    a, b, c = map(int, triangles[i].split())
    if a == 0 and b == 0 and c == 0 :
        break 
    tri_list = [a, b, c]
    max_line = max(tri_list)
    tri_list.remove(max_line)
    
    if tri_list[0]**2 + tri_list[1]**2 == max_line**2 :
        print("right")
    else :
        print("wrong")
    
    