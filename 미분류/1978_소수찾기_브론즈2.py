'''
[정보]
<URL>
https://www.acmicpc.net/problem/1978
<카테고리>
#수학 #정수론 #소수판정

<문제 출처>
백준 제작
'''

#방법 1 : raw하게
#시간 : 16분 20초
'''
[문제 정리 및 계획]
<문제>
N개에서 소수 몇 개?
<입력>
첫줄 : 숫자갯수 : n  (100이하)
두번쨰 : N개의 숫자, 공백   1000이하 자연수
<출력>
갯수
'''
import sys

input_list = [list(map(int, line.split())) for line in sys.stdin.read().splitlines()] #[[],[]]
num_list = input_list[1]
answer = 0
for i in range(len(num_list)) :
    uni_num = True
    if num_list[i] == 1 :
        continue
    for j in range(2, num_list[i]) : 
        if num_list[i] % j == 0 :
            uni_num = False
            break
    if uni_num == False :
        continue
    answer += 1

print(answer)
    
            

'''
[발생한 문제와 해결]

'''

#방법 2 : 알고리즘 사용
#시간 : 
'''
[알고리즘]
<사용할 알고리즘>

<판단이유>

'''


'''
[발생한 문제와 해결]

'''

#방법 3 : 최적의 정답 -> GPT 및 다른 사람들 코드 활용
#시간 : 
'''
[문제 평면화, 일반화]


[문제와 연결하여 분석]

'''



'''
[발생한 문제와 해결]

'''

# 기능 일반화 : 기능 함수화, 수도코드, 배운것 정리
'''

'''
#응용 : 실생활 문제 사례로 문제 재구성

