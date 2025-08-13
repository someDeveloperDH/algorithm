#수학, 구현, 사칙연산
#출처 : solved.ac
# 52%

#방법 1 raw  - 50분, 53%
'''
티셔츠는 S, M, L, XL, XXL, 그리고 XXXL의 6가지 사이즈
티셔츠는 같은 사이즈의 T장 묶음
펜은 한 종류로 P자루씩 묶음으로 주문하거나 한 자루씩 주문

 
N명의 참가자

티셔츠 : 남아도 됨, 부족X, 신청한대로
펜 : 정확히 주문한대로

T장 씩 몇묶음 주문? P자루씩 최대 몇 묶음 및 한 자루 씩 몇개?
'''
'''
<입력>
첫줄 : n명
두번째 : S M L XL XXL XXXL의 신청자 수
세번쨰 : T P

<출력>
T장씩 최소 몇 묶음?
P자루씩 최대 몇 묶음?, 한자루씩 몇개 주문?
'''
import sys

welcome = sys.stdin.read().splitlines() 
n = int(welcome[0])
s,m,l,xl,xxl,xxxl = map(int, welcome [1].split())
size_list = [s,m,l,xl,xxl,xxxl]
t, p = map(int, welcome [2].split())

order_t = 0



# def t_pack_count(size) : 
#     tx = t
#     order = 1
    
#     while size>tx :
#         tx += t
#         order += 1
#     return order

def t_pack_count(size) : 
    if size < t :
        return 1
    else :    
        order = size // t
        if size % t != 0 :
            order += 1
        return order
    

for i in range(len(size_list)) :
    if size_list[i] == 0 :
         continue
    order_t += t_pack_count(size_list[i])
    

order_pSet = n // p
oder_pSurplus = n % p

print(order_t)
print("{} {}".format(order_pSet, oder_pSurplus))

