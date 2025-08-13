'''
#그래프탐색 #그래프이론 #너비우선탐색 #깊이우선탐색 #격자그래프 #플러드 필
'''

# 방법 1 : raw 방식
'''
정사각형, 섬과 바다, 섬의 갯수?
가로 세로 대각선 --> 길
섬은 붙어 있어야만 이동 가능?

<입력>
하나의 입력에 여러 테스트 케이스
첫줄 지도 크기 (w와h 는 50보다 작은 양의 정수)
두번째~ h번째 1 :땅, 0: 바다
입력 마지막줄 : 0 0

<출력>
한줄에 하나씩 섬의 갯수

'''
'''
<입력 분석>
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
하나의 입력에서 각각의 케이스를 분리할 방법?
섬의 범위를 서칭

<출력 분석>
각 테스트 케이스의 섬 갯수 한줄씩
'''
import sys

islandMaps = sys.stdin.read().splitlines() #각 줄이 리스트의 요소 형태(str)로 들어온다.

#print(islandMaps)

#1. 테스트 케이스로 지도 제작
i = 0
while True : 
    #print(i)
    #print(islandMaps[i])
    w, h = map(int, islandMaps[i].split())
    
    if w == 0 and h == 0 :
        break
    
    islandmap = []
    for j in range(i+1, i+1+h) :
        islandmap.append(islandMaps[j])
    #print(islandmap)
    i = i + h + 1
    #2. 섬의 갯수 카운트 (한개의 섬의 크기 파악하기)
    '''
    1 0 1 0 0
    1 0 0 0 0
    1 0 1 0 1
    1 0 0 1 0

    0이면 다음 1을 찾아서 움직이기
    1이면 0으로바꾸고 8방향으로 다른 1이 몇개있나 확인
        1이 없으면 범위 탐색 끝 내고 다음 1로
        1이 한개 이면 움직여서 똑같이 수행
        1이 여러개이면 처음나온 1의 방향으로 가되 나머지 1의 위치 저장

        
    '''
    b = [list(map(int, row.split())) for row in islandmap]
    #print(b)
    #땅의 위치
    c = []
    for x, row in enumerate(b):
        for y, value in enumerate(row):
            if value == 1:
                c.append((x, y))
    #print(c)            
    def search_island_scale(x,y) :
        c.remove((x,y))
        if (x-1,y) in c :
            search_island_scale(x-1,y)        
        if (x-1,y-1) in c :
            search_island_scale(x-1,y-1) 
        if (x-1,y+1) in c :
            search_island_scale(x-1,y+1) 
        if (x,y-1) in c :
            search_island_scale(x,y-1)
        if (x,y+1) in c :
            search_island_scale(x,y+1)
        if (x+1,y) in c :
            search_island_scale(x+1,y)
        if (x+1,y-1) in c :
            search_island_scale(x+1,y-1)
        if (x+1,y+1) in c :
            search_island_scale(x+1,y+1)
        return 1


    total = 0
    while len(c) != 0 : 
        x, y = c[0][0], c[0][1]
        total += search_island_scale(x,y)
        #print(c)

    print(total)


