from vpython import *

# 팀 온보딩 샘플 1단계: 무지개 정원 만들기
# 목표: 어려운 문법 없이 sphere, box, label만 써서 장면을 만든다.

scene_background(color.cyan)

label(pos=vector(0, 3, 0), text="우리 팀의 무지개 정원", height=18, color=color.white)

# 땅
box(pos=vector(0, -0.1, 0), size=vector(8, 0.2, 5), color=color.green)

# 무지개 꽃 7송이
colors = [color.red, color.orange, color.yellow, color.green, color.cyan, color.blue, color.magenta]

for i in range(7):
    x = -3 + i
    sphere(pos=vector(x, 0.45, 0), radius=0.28, color=colors[i])
    box(pos=vector(x, 0.15, 0), size=vector(0.08, 0.6, 0.08), color=color.green)

# 팀원이 이어서 바꿔볼 것:
# 1. 꽃 색 바꾸기
# 2. 꽃 위치 바꾸기
# 3. 하늘에 구름 추가하기
